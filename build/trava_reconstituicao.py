# -*- coding: utf-8 -*-
"""Trava que confere a aritmetica das tabelas de reconstituicao.

POR QUE EXISTE

As tabelas de reconstituicao trazem frasco, agua, concentracao e o volume de
cada dose. Isso e aritmetica fechada:

    volume = dose / concentracao

Nao precisa de fonte externa: a propria tabela se verifica. E um erro aqui e
um erro de dose por fator de 2 ou de 10, que e o modo de falhar que machuca.

Foi assim que a trava nasceu. Em 05/09/2026 uma auditoria manual encontrou,
em 416 celulas, um erro: a tirzepatida trazia "1.125 mL / dividida" onde a
conta da propria tabela dava 1,125 mL -- em portugues, mil cento e vinte e
cinco mililitros. A causa era o encadeamento do dicionario com a regra de
milhar: o dicionario convertia o decimal ingles para virgula, e a regra de
milhar via "1,125" e devolvia "1.125". Auditoria manual nao se repete sozinha;
trava, sim.

OS CINCO FORMATOS

A mesma conta aparece no site em cinco arranjos de tabela. A primeira versao
desta trava so lia o primeiro e cobria 43 tabelas; os outros quatro entraram
em 05/09/2026 e levaram a cobertura a 56 tabelas e 485 celulas.

  F1  concentracao numa coluna, a dose no CABECALHO das colunas seguintes,
      o volume na celula.  ->  volume = dose / concentracao
  F2  dose, concentracao e volume, cada um em sua coluna, na mesma linha.
      ->  volume = dose / concentracao
  F3  o cabecalho declara quantas unidades de insulina se aspira ("10 unidades
      (0,10 mL) entregam") e a celula declara a massa entregue.
      ->  massa = volume x concentracao
  F4  a tabela NAO publica concentracao: publica frasco e agua. A concentracao
      sai da divisao.  ->  volume = dose / (frasco / agua)
  F5  so ha Dose e Volume. A concentracao nao esta escrita em lugar nenhum da
      tabela: e a mediana das razoes dose/volume das proprias linhas. Confere
      so a coerencia interna -- pega uma linha fora da curva, nao pega a tabela
      inteira errada -- e por isso roda com tolerancia mais larga.

OS IDIOMAS (18/09/2026)

Ate 18/09/2026 a trava lia so `p/`, o portugues. As cinco traducoes -- 86
paginas cada, 430 no total -- nunca eram conferidas. O custo apareceu numa
auditoria: o SLU-PP-332 publica "6 unidades (0,06 mL)" onde 250 mcg a 4.000
mcg/mL pedem 0,0625 mL, e o mesmo erro esta nos seis idiomas. Corrigir so o
portugues deixaria cinco paginas erradas no ar.

Traduzir a trava nao e traduzir palavra: e ler NUMERO em cada idioma.

  - pt, es, de  ->  decimal virgula, milhar ponto      "5.000 mcg/mL"
  - en, ja      ->  decimal ponto,  milhar virgula     "5,000 mcg/mL"
  - fr          ->  decimal virgula, milhar ESPACO DURO (U+00A0/U+202F)

Ler "5,000 mcg/mL" do ingles com a regra do portugues devolve 5,0 -- e todo
volume sai com fator 1000. Por isso os separadores NAO sao redeclarados aqui:
vem de `IDIOMAS` em build/idiomas.py, que ja e a fonte de verdade da traducao.
Idioma novo cadastrado la passa a ser conferido aqui sem tocar neste arquivo --
desde que ganhe uma entrada em TERMOS abaixo, com as palavras de cabecalho.
Idioma sem TERMOS nao e' varrido em silencio: a trava avisa.

TRES ARMADILHAS JA PAGAS, que estao no codigo abaixo:

  1. A celula costuma trazer a unidade de insulina ANTES do volume, como em
     "5 unidades (0,05 mL)". Ler o primeiro numero devolve 5 em vez de 0,05,
     e todo divergente sai com fator 100 -- que e exatamente a razao entre
     unidade e mL. Por isso o volume e lido pelo numero que precede "mL".

  2. Em frasco combinado, a concentracao total nao e a de cada peptideo. A
     tabela do CJC-1295 + ipamorelina diz "10,0 mg/mL no total (5,0 mg/mL de
     cada)" e tem coluna propria "Por peptideo". A dose e de cada um, entao a
     conta usa a concentracao por peptideo. Tabela com "de cada" ou "por
     peptideo" no cabecalho da concentracao usa o menor valor da celula.

  3. No F3 a mesma confusao aparece pelo avesso: no KLOW a concentracao
     publicada e a do blend inteiro ("Concentracao total", 40 mg/mL) e a
     coluna nomeia UM componente ("GHK-Cu por unidade", ~250 mcg). A conta
     0,01 mL x 40 mg/mL = 400 mcg esta certa para o blend e errada para o
     GHK-Cu: 250 + 50 x 3 = 400. Sao os quatro componentes. Coluna de
     componente contra concentracao total nao se confere -- se pula.

Roda sozinha (`python build/trava_reconstituicao.py`) e no hook de pre-commit.
Codigo de saida 1 em caso de divergencia.
"""
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from idiomas import IDIOMAS, PT          # separadores numericos: fonte unica

TOLERANCIA = 0.05          # 5%: absorve arredondamento de tabela
TOLERANCIA_F5 = 0.10       # concentracao inferida da propria tabela: mais folga
CONC_GENERICA = re.compile("oncentra|onzentration|濃度|浓度")

# Palavras de cabecalho por idioma. O que muda de um idioma para outro e' so'
# isto e o separador numerico (que vem de idiomas.IDIOMAS).
#
#   recon   titulo da tabela de reconstituicao
#   agua    coluna da agua bacteriostatica
#   conc    coluna da concentracao
#   frasco  coluna do frasco
#   dose    coluna da dose (F2/F5)
#   vol     coluna do volume (F2/F5)
#   uni     "unidade" de seringa, no cabecalho do F3
#   comb    frasco combinado: "de cada" / "por peptideo" (armadilha 2)
#   total   "total" do blend, que a armadilha 3 usa para NAO conferir coluna
#           de um componente contra a concentracao da mistura inteira
#
# Verificados contra os cabecalhos realmente publicados em cada idioma, em
# 18/09/2026.
TERMOS = {
    'pt': dict(recon=r"reconstitui", agua=r"gua bacteriost", conc=r"oncentra",
               frasco=r"frasco|vial", dose=r"dose|quantidade de pesquisa|quantidade-alvo",
               vol=r"volume|aspirar", uni=r"unidade", comb=r"de cada|por pept",
               total=r"total"),
    'en': dict(recon=r"reconstitution", agua=r"BAC water|bacteriostatic", conc=r"oncentration",
               frasco=r"vial", dose=r"dose|dosage|target amount|research amount",
               vol=r"volume|draw", uni=r"unit", comb=r"of each|each|per pept",
               total=r"total"),
    'es': dict(recon=r"reconstituci", agua=r"gua bacteriost", conc=r"oncentraci",
               frasco=r"vial|frasco", dose=r"dosis|cantidad",
               vol=r"volumen|extraer", uni=r"unidad", comb=r"cada|por p",
               total=r"total"),
    'fr': dict(recon=r"reconstitution", agua=r"Eau bact", conc=r"oncentration",
               frasco=r"flacon|vial", dose=r"dose",
               vol=r"volume|pr.lever", uni=r"unit", comb=r"chacun|chaque|par pept",
               total=r"total"),
    # "von jedem" e' o "de cada" alemao -- sem ele a tabela do CJC-1295 +
    # ipamorelina confere a dose por peptideo contra a concentracao do blend.
    'de': dict(recon=r"Rekonstitution", agua=r"akteriostat", conc=r"onzentration",
               frasco=r"vial|Durchstechflasche", dose=r"Dosis|Dosierung|Zielmenge",
               vol=r"Volumen|ufzuziehende", uni=r"Einheit",
               comb=r"von jedem|jeweils|je Peptid|pro Peptid", total=r"gesamt"),
    'ja': dict(recon=r"溶解", agua=r"静菌水", conc=r"濃度",
               frasco=r"バイアル", dose=r"用量|投与量",
               vol=r"容量|吸引", uni=r"単位", comb=r"各|ごと", total=r"総|合計|全体"),
    # Escritos antes de o chines existir e conferidos na primeira geracao, em
    # 18/09/2026: a trava reconhece 71 tabelas em /zh/, a mesma contagem do
    # japones. Se um dia cair para zero, o termo errado esta aqui, nao no site.
    'zh': dict(recon=r"复溶|溶解", agua=r"抑菌", conc=r"浓度",
               frasco=r"西林瓶|小瓶|瓶", dose=r"剂量|用量",
               vol=r"体积|抽取量|容量", uni=r"单位", comb=r"每种|各",
               total=r"总|合计"),
}


def _locais():
    """(codigo, subpasta, regex compilados) de cada idioma conferivel.

    O portugues mora na raiz; cada traducao, em /<codigo>/. Os separadores vem
    de idiomas.py; as palavras, de TERMOS. Idioma cadastrado em IDIOMAS sem
    entrada em TERMOS entra na lista de avisos -- nunca e' pulado calado."""
    faltando = []
    for cod, cfg in [('pt', PT)] + list(IDIOMAS.items()):
        t = TERMOS.get(cod)
        if t is None:
            faltando.append(cod)
            continue
        dec, mil = cfg['decimal'], cfg['milhar']
        # o numero pode trazer o separador de milhar no meio e o decimal no fim
        corpo = "".join(re.escape(c) for c in dict.fromkeys(mil))
        num = r"(\d[\d%s]*(?:%s\d+)?)" % (corpo, re.escape(dec))
        yield cod, ('p' if cod == 'pt' else os.path.join(cod, 'p')), dict(
            dec=dec, mil=mil,
            NUM=re.compile(num),
            VOL=re.compile(num + r"\s*mL"),
            UNI=re.compile(num + r"\s*(?:%s)" % t['uni']),
            CONC=re.compile(t['conc']),
            CAB_DOSE=re.compile(t['dose'], re.I),
            CAB_VOL=re.compile(t['vol'], re.I),
            CAB_AGUA=re.compile(t['agua'], re.I),
            CAB_FRASCO=re.compile(t['frasco'], re.I),
            COMBINADO=re.compile(t['comb'], re.I),
            RECON=re.compile(t['recon'], re.I),
            TOTAL=re.compile(t['total'], re.I),
        )
    if faltando:
        print("AVISO: idioma(s) em IDIOMAS sem entrada em TERMOS, nao conferido(s): %s"
              % ", ".join(faltando), file=sys.stderr)


def limpo(c):
    """Normaliza o espaco em branco MENOS o espaco duro.

    Armadilha 4, paga em 18/09/2026: `\\s` do Python casa U+00A0, entao o
    `\\s+` de antes transformava o "5<U+00A0>000 mcg/mL" do frances em
    "5 000 mcg/mL" -- espaco comum -- e o separador de milhar sumia antes de
    qualquer regra de numero rodar. A concentracao virava 333 em vez de 3.333
    e toda a tabela francesa saia divergente com fator 0,10."""
    c = re.sub("<[^>]+>", "", c)
    return re.sub(r"[^\S  ]+", " ", c).strip()


def numero(txt, L):
    """'5.000' -> 5000.0 em pt/es/de ; '5,000' -> 5000.0 em en/ja ;
    '5<NBSP>000' -> 5000.0 em fr. Le pelo separador do proprio idioma."""
    for c in L['mil']:
        txt = txt.replace(c, "")
    return float(txt.replace(L['dec'], "."))


def massa_mcg(txt, L, menor=False):
    """Converte a primeira massa do texto para mcg. Com menor=True, usa a
    menor de todas -- e o caso do frasco combinado, em que o cabecalho traz
    o total e o valor por peptideo na mesma celula."""
    vals = []
    for m in L['NUM'].finditer(txt):
        try:
            v = numero(m.group(1), L)
        except ValueError:
            continue
        resto = txt[m.end():m.end() + 8]
        if re.match(r"\s*mg", resto):
            vals.append(v * 1000)
        elif re.match(r"\s*(mcg|µg)", resto):
            vals.append(v)
    if not vals:
        return None
    return min(vals) if menor else vals[0]


def volume(txt, L):
    """O volume e o numero que PRECEDE 'mL' -- ver armadilha 1."""
    m = L['VOL'].search(txt)
    if not m:
        return None
    try:
        return numero(m.group(1), L)
    except ValueError:
        return None


def coluna(cab, rx):
    return next((i for i, c in enumerate(cab) if rx.search(c)), None)


def _tabelas(raiz):
    """Devolve (idioma, regex, arquivo, legenda, cabecalho, linhas) de cada
    tabela de reconstituicao publicada, em todos os idiomas."""
    for cod, sub, L in _locais():
        for f in sorted(glob.glob(os.path.join(raiz, sub, "*.html"))):
            h = io.open(f, encoding="utf-8", errors="replace").read()
            for cap, bloco in re.findall(
                    r'<div class="tabela-titulo">(.*?)</div>(.*?)</table>', h, re.S):
                if not L['RECON'].search(cap):
                    continue
                linhas = re.findall(r"<tr>(.*?)</tr>", bloco, re.S)
                if len(linhas) < 2:
                    continue
                celulas = [[limpo(c) for c in
                            re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", l, re.S)]
                           for l in linhas]
                nome = os.path.basename(f) if cod == 'pt' else "%s/%s" % (cod, os.path.basename(f))
                yield L, nome, limpo(cap)[:40], celulas[0], celulas[1:]


def checar(raiz=RAIZ):
    faltas = []
    tabelas = celulas = 0

    def erra(fmt, rot, msg):
        faltas.append("%s [%s] %s" % (rot, fmt, msg))

    for L, arq, cap, cab, corpo in _tabelas(raiz):
        rot = "%s | %s" % (arq, cap)
        i_conc = coluna(cab, L['CONC'])
        i_dose = coluna(cab, L['CAB_DOSE'])
        i_vol = coluna(cab, L['CAB_VOL'])
        n = 0

        # -------------------------------------------------- F1
        if i_conc is not None:
            doses = {i: massa_mcg(c, L) for i, c in enumerate(cab)
                     if i > i_conc and massa_mcg(c, L)}
            if doses:
                combinado = bool(L['COMBINADO'].search(cab[i_conc]))
                for cels in corpo:
                    if len(cels) <= i_conc:
                        continue
                    tc = cels[i_conc]
                    conc = massa_mcg(tc, L, menor=combinado or bool(L['COMBINADO'].search(tc)))
                    if not conc:
                        continue
                    for i, dose in doses.items():
                        if i >= len(cels):
                            continue
                        vol = volume(cels[i], L)
                        if vol is None:
                            continue
                        n += 1
                        esperado = dose / conc
                        if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA:
                            erra("F1", rot,
                                 "concentracao %g mcg/mL, dose %g mcg: a tabela diz "
                                 "%g mL e a conta da %.4g mL (fator %.2f)"
                                 % (conc, dose, vol, esperado, vol / esperado))
                if n:
                    tabelas += 1
                    celulas += n
                    continue

        # -------------------------------------------------- F2
        if (i_conc is not None and i_dose is not None and i_vol is not None
                and i_dose != i_conc and i_vol != i_conc):
            for cels in corpo:
                if max(i_dose, i_vol, i_conc) >= len(cels):
                    continue
                dose = massa_mcg(cels[i_dose], L)
                conc = massa_mcg(cels[i_conc], L)
                vol = volume(cels[i_vol], L)
                if not (dose and conc and vol is not None):
                    continue
                n += 1
                esperado = dose / conc
                if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA:
                    erra("F2", rot,
                         "concentracao %g mcg/mL, dose %g mcg: a tabela diz %g mL "
                         "e a conta da %.4g mL (fator %.2f)"
                         % (conc, dose, vol, esperado, vol / esperado))
            if n:
                tabelas += 1
                celulas += n
                continue

        # -------------------------------------------------- F3
        if i_conc is not None:
            for j, ch in enumerate(cab):
                if j == i_conc:
                    continue
                mu, mvh = L['UNI'].search(ch), L['VOL'].search(ch)
                if not (mu or mvh):
                    continue
                try:
                    vol_cab = (numero(mvh.group(1), L) if mvh
                               else numero(mu.group(1), L) / 100.0)
                except ValueError:
                    continue
                for cels in corpo:
                    if max(j, i_conc) >= len(cels):
                        continue
                    tc, tx = cels[i_conc], cels[j]
                    # celula que soma componentes, ou que fala de cada um.
                    # O japones usa o mais de largura inteira (U+FF0B).
                    if "+" in tx or "＋" in tx or L['COMBINADO'].search(tx):
                        continue
                    # armadilha 3: coluna de componente contra concentracao total.
                    # "total" muda de idioma: gesamt, 総/合計, 总/合计.
                    if (L['TOTAL'].search(tc + " " + cab[i_conc])
                            and not L['TOTAL'].search(tx + " " + ch)):
                        continue
                    conc, massa = massa_mcg(tc, L), massa_mcg(tx, L)
                    if not (conc and massa):
                        continue
                    vc = volume(tx, L)
                    vol = vc if vc is not None else vol_cab
                    n += 1
                    esperado = vol * conc
                    if esperado > 0 and abs(massa - esperado) / esperado > TOLERANCIA:
                        erra("F3", rot,
                             "'%s': %g mL x %g mcg/mL da %.4g mcg e a tabela diz "
                             "%g mcg (fator %.2f)"
                             % (ch[:30], vol, conc, esperado, massa, massa / esperado))
            if n:
                tabelas += 1
                celulas += n
                continue

        # -------------------------------------------------- F4
        i_agua, i_frasco = coluna(cab, L['CAB_AGUA']), coluna(cab, L['CAB_FRASCO'])
        if i_agua is not None and i_frasco is not None and i_agua != i_frasco:
            doses = {i: massa_mcg(c, L) for i, c in enumerate(cab)
                     if i not in (i_agua, i_frasco) and massa_mcg(c, L)}
            if doses:
                for cels in corpo:
                    if max(i_agua, i_frasco) >= len(cels):
                        continue
                    frasco = massa_mcg(cels[i_frasco], L)
                    agua = volume(cels[i_agua], L)
                    if not frasco or not agua:
                        continue
                    conc = frasco / agua
                    for i, dose in doses.items():
                        if i >= len(cels):
                            continue
                        vol = volume(cels[i], L)
                        if vol is None:
                            continue
                        n += 1
                        esperado = dose / conc
                        if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA:
                            erra("F4", rot,
                                 "frasco %g mcg em %g mL da %g mcg/mL; dose %g mcg "
                                 "pede %.4g mL e a tabela diz %g mL (fator %.2f)"
                                 % (frasco, agua, conc, dose, esperado, vol,
                                    vol / esperado))
                if n:
                    tabelas += 1
                    celulas += n
                    continue

        # -------------------------------------------------- F5
        if (i_conc is None and i_dose is not None and i_vol is not None
                and i_dose != i_vol):
            pares = []
            for cels in corpo:
                if max(i_dose, i_vol) >= len(cels):
                    continue
                dose, vol = massa_mcg(cels[i_dose], L), volume(cels[i_vol], L)
                if dose and vol:
                    pares.append((dose, vol))
            # com menos de tres linhas a mediana nao tem de onde sair
            if len(pares) >= 3:
                razoes = sorted(d / v for d, v in pares)
                conc = razoes[len(razoes) // 2]
                tabelas += 1
                celulas += len(pares)
                for dose, vol in pares:
                    esperado = dose / conc
                    if esperado > 0 and abs(vol - esperado) / esperado > TOLERANCIA_F5:
                        erra("F5", rot,
                             "as linhas da tabela dao %g mcg/mL; nessa concentracao "
                             "a dose de %g mcg pede %.4g mL e a tabela diz %g mL "
                             "(fator %.2f)"
                             % (conc, dose, esperado, vol, vol / esperado))

    return faltas, tabelas, celulas


def main():
    faltas, tabelas, celulas = checar()
    if faltas:
        print("TRAVA DE RECONSTITUICAO: %d divergencia(s)\n" % len(faltas), file=sys.stderr)
        for f in faltas:
            print("  " + f, file=sys.stderr)
        print("\nvolume = dose / concentracao. Leia o cabecalho de "
              "build/trava_reconstituicao.py.", file=sys.stderr)
        return 1
    print("trava de reconstituicao: ok (%d tabelas, %d celulas)" % (tabelas, celulas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
