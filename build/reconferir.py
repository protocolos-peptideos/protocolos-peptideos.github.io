# -*- coding: utf-8 -*-
"""Reexecuta toda consulta declarada no site e avisa o que divergiu da base.

Por que existe: a trava de consultas garante que todo numero publicado venha com
a consulta que o produziu. Isso torna o site conferivel -- mas nao impede que os
numeros ENVELHECAM em silencio. O PubMed indexa artigo novo todo dia; uma
contagem correta em setembro pode estar velha em dezembro, sem que nada no
repositorio mude.

Este script fecha esse buraco: le as consultas do proprio conteudo, roda cada
uma, e compara com o que esta publicado.

    python build/reconferir.py              relatorio na tela
    python build/reconferir.py --json f.json  grava tambem em JSON
    python build/reconferir.py --limiar 5    tolera 5% de variacao
    python build/reconferir.py --pagina proprio_leste   so uma pagina

O QUE ELE NAO FAZ, DE PROPOSITO: nao corrige nada. A tentacao obvia seria
reescrever os numeros sozinho -- e ai o site passaria a afirmar, com a data de
apuracao antiga, resultados colhidos em outro dia. Numero e data de apuracao
andam juntos: quem atualiza um atualiza o outro, e isso e decisao de quem
apura, nao de um script agendado. Ver o cabecalho de build/datas.py.

Codigo de saida: 0 se nada divergiu alem do limiar, 1 se algo divergiu -- para
servir de gatilho em tarefa agendada.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
CTGOV = "https://clinicaltrials.gov/api/v2/studies"
PAUSA = 0.34          # PubMed tolera 3 req/s sem chave de API
TENTATIVAS = 3


def _txt(x):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(x))).strip()


def conta_pubmed(termo):
    q = urllib.parse.urlencode({"db": "pubmed", "term": termo,
                                "rettype": "count", "retmode": "json"})
    for _ in range(TENTATIVAS):
        try:
            r = urllib.request.urlopen(f"{EUTILS}?{q}", timeout=30).read().decode()
            return int(json.loads(r)["esearchresult"]["count"])
        except Exception:
            time.sleep(2)
    return None


def conta_ctgov(termo, campo="intr", extra=None):
    """No ClinicalTrials.gov, buscar por condicao e por intervencao sao coisas
    diferentes e devolvem numeros diferentes. A pagina diz qual usou, e o
    script obedece: 'condição X' vira query.cond, 'termo livre' vira
    query.term, o resto vira query.intr. `extra` junta mais campos na mesma
    busca ("intervenção: `A`; condição: `B`")."""
    params = {f"query.{campo}": termo}
    for c, t in (extra or {}).items():
        params[f"query.{c}"] = t
    q = urllib.parse.urlencode({**params, "countTotal": "true", "pageSize": 1})
    for _ in range(TENTATIVAS):
        try:
            r = urllib.request.urlopen(f"{CTGOV}?{q}", timeout=30).read().decode()
            return json.loads(r).get("totalCount")
        except Exception:
            time.sleep(2)
    return None


def _campo(rotulo, padrao):
    """Campo de busca do ClinicalTrials.gov dito no rotulo antes do <code>."""
    t = rotulo.lower()
    if "termo" in t or "query.term" in t or "busca livre" in t:
        return "term"
    if "intervenç" in t or "intervenc" in t:
        return "intr"
    if "condi" in t or "condition" in t:
        return "cond"
    return padrao


def alvos(PROPRIOS):
    """Toda linha de tabela que traz consulta em <code> ao lado de um numero."""
    achados = []
    for slug, pagina in PROPRIOS.items():
        for sec in pagina["secoes"]:
            tab = sec.get("tabela")
            if not tab:
                continue
            cab = [_txt(c).lower() for c in tab["linhas"][0]]
            i_consulta = next((k for k, c in enumerate(cab) if "consulta" in c), None)
            if i_consulta is None:
                continue
            i_base = next((k for k, c in enumerate(cab) if c == "base"), None)
            # colunas de numero, com a base que cada uma representa
            cols = []
            for k, c in enumerate(cab):
                if k == i_consulta:
                    continue
                if "clinicaltrials" in c or "ensaios registrados" in c:
                    cols.append((k, "ctgov"))
                elif "pubmed" in c or "artigo" in c or "resultado" in c:
                    cols.append((k, "pubmed"))
            for linha in tab["linhas"][1:]:
                bruto = str(linha[i_consulta])
                cod = re.findall(r"<code>(.*?)</code>", bruto, re.S)
                if not cod:
                    continue
                consulta = _txt(cod[0])
                # o texto fora do <code> diz se a busca foi por condicao
                rotulo_consulta = _txt(re.sub(r"<code>.*?</code>", " ", bruto, flags=re.S)).lower()
                campo = "cond" if ("condi" in rotulo_consulta
                                   or "condition" in rotulo_consulta) else "intr"
                # Rotulo explicito antes de cada <code> ("termo livre: `A`",
                # "intervenção: `A`; condição: `B`") manda mais que a regra
                # acima, que olha a celula inteira. Sem rotulo explicito, nada muda.
                pedacos = re.split(r"<code>.*?</code>", bruto, flags=re.S)
                campo = _campo(_txt(pedacos[0]), campo)
                extra = {}
                for k in range(1, len(cod)):
                    c2 = _campo(_txt(pedacos[k]), None)
                    if c2 and c2 != campo:
                        extra[c2] = _txt(cod[k])
                base_linha = _txt(linha[i_base]).lower() if i_base is not None else ""
                for k, base in cols:
                    if k >= len(linha):
                        continue
                    m = re.match(r"([\d][\d\.]*)", _txt(linha[k]))
                    if not m:
                        continue
                    b = base
                    if base_linha:
                        b = "ctgov" if "clinicaltrials" in base_linha else "pubmed"
                    achados.append(dict(
                        slug=slug, tabela=tab.get("cap", "?"),
                        rotulo=_txt(linha[0])[:44], coluna=cab[k], base=b,
                        consulta=consulta, campo=campo, extra=extra,
                        publicado=int(m.group(1).replace(".", ""))))
    return achados


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", metavar="ARQ", help="grava o relatorio tambem em JSON")
    ap.add_argument("--limiar", type=float, default=2.0,
                    help="variacao percentual tolerada (padrao 2%%)")
    ap.add_argument("--quieto", action="store_true", help="so o resumo e as divergencias")
    ap.add_argument("--pagina", metavar="SLUG",
                    help="reconfere so uma pagina, p.ex. proprio_leste")
    args = ap.parse_args()

    from datas import DATA_APURACAO
    from proprios import PROPRIOS

    itens = alvos(PROPRIOS)
    if args.pagina:
        itens = [i for i in itens if i["slug"] == args.pagina]
        if not itens:
            print(f"nenhuma contagem com consulta declarada em '{args.pagina}'")
            return 0
    print(f"Reconferência de {len(itens)} contagens publicadas.")
    print(f"Data de apuração declarada no site: {DATA_APURACAO}\n")

    saida, n_ok, n_osc, n_dif, n_erro = [], 0, 0, 0, 0
    for it in itens:
        if it["base"] == "pubmed":
            agora = conta_pubmed(it["consulta"])
        else:
            agora = conta_ctgov(it["consulta"], it.get("campo", "intr"), it.get("extra"))
        time.sleep(PAUSA)
        pub = it["publicado"]
        if agora is None:
            veredito, n_erro = "ERRO", n_erro + 1
        elif agora == pub:
            veredito, n_ok = "igual", n_ok + 1
        elif abs(agora - pub) <= max(1, pub * args.limiar / 100):
            veredito, n_osc = "oscilou", n_osc + 1
        else:
            veredito, n_dif = "DIVERGE", n_dif + 1
        it.update(agora=agora, veredito=veredito)
        saida.append(it)
        if veredito in ("DIVERGE", "ERRO") or not args.quieto:
            marca = {"igual": "  ", "oscilou": " ~", "DIVERGE": " !", "ERRO": " ?"}[veredito]
            print(f" {marca} {it['slug'][:22]:22} {it['rotulo'][:26]:26} "
                  f"pub={pub:>6} agora={str(agora):>6}  {it['consulta'][:44]}")

    print(f"\n  iguais {n_ok} · oscilaram dentro de {args.limiar}% {n_osc} · "
          f"DIVERGEM {n_dif} · erro de rede {n_erro}")

    if n_dif:
        print("\n  O que fazer: refazer o levantamento das linhas acima e publicar")
        print("  o número novo JUNTO com a data de apuração nova, em build/datas.py.")
        print("  Número novo com data velha é pior que número velho: afirma que")
        print("  alguém conferiu num dia em que ninguém conferiu.")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(dict(data_apuracao_do_site=DATA_APURACAO, itens=saida),
                      f, ensure_ascii=False, indent=1)
        print(f"\n  relatório em {args.json}")

    return 1 if n_dif else 0


if __name__ == "__main__":
    sys.exit(main())
