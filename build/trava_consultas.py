# -*- coding: utf-8 -*-
"""Trava que impede publicar contagem de levantamento sem a consulta que a produziu.

Nasceu de uma auditoria em 04/09/2026. Ao reexecutar as consultas que as
proprias paginas declaravam, uma delas nao reproduziu: estava publicada como
"… AND (Clinical Trial[Publication Type] ...)", com reticencias no lugar do
termo inicial. Quem copiasse receberia 1.059.391 em vez de 35, porque o PubMed
ignora a elipse. O numero da pagina estava certo; o que estava quebrado era a
possibilidade de conferir.

E isso que esta trava protege: **contagem publicada tem que ser reproduzivel por
quem le**. Nao basta o numero estar correto -- se o leitor nao consegue repetir
a busca, o numero e uma afirmacao de autoridade, que e exatamente o que este
site cobra dos outros.

Tres regras, checadas sobre o CONTEUDO carregado (PROPRIOS), nao sobre o codigo:

  1. Consulta declarada nao pode ser abreviada. Proibido elipse, "idem",
     "mesma consulta" e afins dentro de uma consulta. Ou escreve inteira, ou
     nao e consulta.

  2. Tabela que publica contagem de base bibliografica precisa declarar a
     consulta: coluna "Consulta" na propria tabela, ou a consulta literal em
     <code> no texto da secao.

  3. Filtro citado por apelido -- "ECR/meta", "ensaio clinico" como nome de
     coluna -- precisa ter a expressao literal escrita em <code> em algum lugar
     da mesma pagina. Apelido de coluna nao reproduz busca.

O que esta trava NAO faz, deliberadamente: nao acusa numero que e conteudo de
terceiro. "A meta-analise reuniu 21 estudos" e fato reportado, nao levantamento
proprio, e nao tem consulta para declarar. Uma primeira versao desta trava
acusava 12 ocorrencias das quais 9 eram desse tipo -- e trava que acusa o
legitimo ensina a ser ignorada. A regra so olha TABELA, onde a contagem e
inequivocamente um levantamento do site.

Roda sozinha (`python build/trava_consultas.py`) e tambem no inicio do
gerar.py, que aborta se falhar. Codigo de saida 1 em caso de violacao.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

# bases cujas contagens sao levantamento do site
BASES = ("pubmed", "clinicaltrials")

# marcas de consulta abreviada -- o bug que originou a trava
ABREVIACOES = ("…", "...", "[idem]", "idem,", "idem ", "mesma consulta",
               "same as above", "ibid")

# apelidos de filtro que precisam da expressao literal em algum lugar da pagina
APELIDOS = {
    "ecr/meta": ("randomized controlled trial[publication type]", "meta-analysis[publication type]"),
    "ensaio clínico": ("clinical trial[publication type]",),
    "ensaios clínicos": ("clinical trial[publication type]",),
}


def _txt(x):
    """Texto visivel de uma celula ou paragrafo."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(x))).strip()


def _codigos(*blocos):
    """Todo conteudo marcado como <code> nos blocos dados, em minusculas."""
    achado = []
    for b in blocos:
        achado += re.findall(r"<code>(.*?)</code>", str(b), re.S | re.I)
    return [re.sub(r"\s+", " ", _txt(c)).lower() for c in achado]


# ---------------------------------------------------------------------------
# DIVIDA: vazia.
#
# Quatro tabelas nasceram antes desta trava e publicavam contagem sem a consulta
# que a produziu. Em 04/09/2026 os quatro levantamentos foram REFEITOS, com a
# consulta de cada linha definida, rodada e publicada ao lado do numero.
#
# Ficou de licao o caso do ligandrol: buscando "LGD-4033 OR ligandrol" no
# ClinicalTrials.gov o resultado e zero, e a pagina teria afirmado que o
# composto nunca entrou em ensaio. O ensaio existe -- fase 2, 108 participantes,
# fratura de quadril -- registrado sob o sinonimo VK5211. Consulta declarada nao
# serve so para o leitor conferir: serve para quem escreve perceber que a busca
# estava incompleta.
DIVIDA = set()


def confere(PROPRIOS):
    falhas, pendentes = [], []

    for slug, pagina in PROPRIOS.items():
        secoes = pagina["secoes"]
        # tudo que a pagina marca como <code>, para a regra 3
        code_pagina = _codigos(*[c for s in secoes for c in s["corpo"]],
                               *[str(l) for s in secoes if s.get("tabela")
                                 for l in s["tabela"]["linhas"]])

        for i, sec in enumerate(secoes):
            tab = sec.get("tabela")
            if not tab:
                continue
            cab = [_txt(c).lower() for c in tab["linhas"][0]]
            cap = tab.get("cap", f"secao {i}")
            herdada = (slug, cap) in DIVIDA
            saco = pendentes if herdada else falhas
            code_secao = _codigos(*sec["corpo"], *[str(l) for l in tab["linhas"]])
            tem_col_consulta = any("consulta" in c for c in cab)

            # ---------------------------------------------- regra 1
            for consulta in code_secao:
                for marca in ABREVIACOES:
                    # "ibid" so como palavra: "libido" contem "ibid" e e consulta legitima
                    if (re.search(r"(?<![a-z])ibid(?![a-z])", consulta) if marca == "ibid"
                            else marca in consulta):
                        saco.append(
                            f"{slug} · tabela '{cap}': consulta abreviada com "
                            f"'{marca.strip()}' — escreva a consulta inteira, "
                            f"senão ela não reproduz.\n      {consulta[:100]}")

            # ---------------------------------------------- regra 2
            col_base = [c for c in cab if any(b in c for b in BASES)]
            tem_contagem = False
            if col_base:
                idx = [k for k, c in enumerate(cab) if any(b in c for b in BASES)]
                for linha in tab["linhas"][1:]:
                    for k in idx:
                        if k < len(linha) and re.fullmatch(r"[\d\.]+", _txt(linha[k])):
                            tem_contagem = True
            if tem_contagem and not tem_col_consulta and not code_secao:
                saco.append(
                    f"{slug} · tabela '{cap}': publica contagem de "
                    f"{', '.join(col_base)} sem declarar a consulta. Acrescente "
                    f"coluna 'Consulta' ou escreva a busca em <code> no texto "
                    f"da seção.")

            # ---------------------------------------------- regra 3
            if tem_contagem:
                for apelido, literais in APELIDOS.items():
                    if any(apelido in c for c in cab):
                        if not any(any(lit in cp for cp in code_pagina) for lit in literais):
                            saco.append(
                                f"{slug} · tabela '{cap}': a coluna "
                                f"'{apelido}' é apelido de filtro. Escreva a "
                                f"expressão literal em <code> na página — "
                                f"esperado algo como '{literais[0]}'.")
    return falhas, pendentes


def main():
    from proprios import PROPRIOS
    falhas, pendentes = confere(PROPRIOS)
    if pendentes:
        print(f"trava de consultas: {len(pendentes)} pendência(s) herdada(s), "
              f"em {len(DIVIDA)} tabelas anteriores à trava:")
        for p in pendentes:
            print(f"  · {p}")
        print("  Sair daqui exige refazer o levantamento e publicar consulta e "
              "número juntos.\n")
    if falhas:
        print("trava de consultas: FALHOU\n")
        for f in falhas:
            print(f"  - {f}")
        print(f"\n{len(falhas)} violação(ões). Contagem publicada tem que ser "
              f"reproduzível por quem lê.")
        return 1
    print("trava de consultas: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
