# -*- coding: utf-8 -*-
"""Prova que a trava de reconstituicao PEGA erro, em cada formato e cada idioma.

Cobertura sem poder de deteccao nao vale nada: uma trava que le 2.868 celulas e
nunca acusaria nada passaria neste site exatamente como a de verdade. Este
teste separa as duas coisas.

Copia p/ e as pastas de idioma para uma pasta temporaria, injeta UM erro de
dose por vez -- sempre um fator de 10, que e o modo de falhar que machuca -- e
verifica que a trava acusa no formato certo. O primeiro caso e o bug real de
05/09/2026, na tirzepatida, que deu origem a trava; os quatro seguintes cobrem
os formatos que entraram depois; os cinco ultimos cobrem um idioma cada,
acrescentados em 18/09/2026 junto com a varredura das traducoes.

Antes da injecao roda uma prova de leitura de numero por idioma. E o que
separa "a trava nao acusou nada" de "a trava nao conseguiu ler nada": o
frances escreve cinco mil como "5<U+00A0>000" e o ingles como "5,000"; lido
com a regra do portugues, o primeiro vira 5 e o segundo vira 5,0 -- e a trava
passaria calada por uma tabela inteira errada.

O site original nunca e tocado: a copia e apagada no fim.

    python build/testa_reconstituicao.py

Codigo de saida 1 se algum erro injetado passar batido.
"""
import io, os, re, shutil, sys, tempfile
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import trava_reconstituicao as T

# (nome, caminho dentro do site, trecho original, trecho com erro)
CASOS = [
    # o bug original de 05/09/2026, que deu origem a trava: regressao do F1
    ("F1 Tirzepatida", "p/protocol_tirzepatide.html", '<td class="num">1,125 mL / dividida</td>',
                                                      '<td class="num">1.125 mL / dividida</td>'),
    ("F2 GHRP-6",      "p/protocol_ghrp-6.html",      '<td class="num">0,06 mL</td>',        '<td class="num">0,60 mL</td>'),
    ("F3 Pinealon",    "p/protocol_pinealon.html",    '0,10 mg (100 mcg)',                   '1,00 mg (1000 mcg)'),
    ("F4 Semaglutide", "p/protocol_semaglutide.html", '<td class="num">0,20 mL (20 u)</td>', '<td class="num">2,00 mL (20 u)</td>'),
    ("F5 LL-37",       "p/protocol_ll-37.html",       '<td class="num">0,08 mL</td>',        '<td class="num">0,80 mL</td>'),
    # um por idioma (18/09/2026). Mesma pagina em cinco deles, de proposito:
    # o que muda e' a leitura do numero e das palavras de cabecalho, nao a conta.
    # O chines usa parentese de largura inteira: a ancora e' '（', nao '('.
    ("F1 EN PT-141",   "en/p/protocol_bremelanotide-pt-141.html", '>0.175 mL (', '>1.75 mL ('),
    ("F1 ES PT-141",   "es/p/protocol_bremelanotide-pt-141.html", '>0,175 mL (', '>1,75 mL ('),
    ("F1 DE PT-141",   "de/p/protocol_bremelanotide-pt-141.html", '>0,175 mL (', '>1,75 mL ('),
    ("F1 FR PT-141",   "fr/p/protocol_bremelanotide-pt-141.html", '>0,175 mL (', '>1,75 mL ('),
    ("F1 JA Melanotan", "ja/p/protocol_melanotan-ii.html",        '>0.025 mL (', '>0.25 mL ('),
    ("F1 ZH PT-141",   "zh/p/protocol_bremelanotide-pt-141.html", '>0.175 mL（', '>1.75 mL（'),
]

# "cinco mil" escrito em cada idioma. Se a leitura falhar aqui, a trava esta
# cega naquele idioma -- e silencio nao e' aprovacao.
CINCO_MIL = {'pt': '5.000', 'en': '5,000', 'es': '5.000',
             'de': '5.000', 'fr': '5 000', 'ja': '5,000', 'zh': '5,000'}

base = tempfile.mkdtemp(prefix="trava-inj-")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- numeros
print("leitura de numero por idioma:")
falhou = False
for cod, sub, L in T._locais():
    amostra = CINCO_MIL.get(cod)
    if amostra is None:
        print("  %-3s SEM AMOSTRA em CINCO_MIL -- acrescente uma" % cod)
        falhou = True
        continue
    try:
        v = T.numero(amostra, L)
    except ValueError as e:
        v, e = None, e
    ok = (v == 5000.0)
    print("  %-3s %-10r -> %-8s %s" % (cod, amostra, v, "ok" if ok else "ERRADO"))
    if not ok:
        falhou = True
print()

# ---------------------------------------------------------------- copia
shutil.copytree(os.path.join(RAIZ, "p"), os.path.join(base, "p"))
for cod in T.IDIOMAS:
    orig_dir = os.path.join(RAIZ, cod, "p")
    if os.path.isdir(orig_dir):
        shutil.copytree(orig_dir, os.path.join(base, cod, "p"))

f, t, c = T.checar(base)
print("copia limpa: %d tabelas, %d celulas, %d divergencias" % (t, c, len(f)))
assert not f, "a copia limpa ja acusa: %s" % f
print()

# ---------------------------------------------------------------- injecao
for nome, rel, de, para in CASOS:
    p = os.path.join(base, *rel.split("/"))
    if not os.path.exists(p):
        print("%-18s ARQUIVO AUSENTE (%s)" % (nome, rel))
        falhou = True
        continue
    orig = io.open(p, encoding="utf-8").read()
    if de not in orig:
        print("%-18s NAO CONSEGUI INJETAR (nao achei %r)" % (nome, de))
        falhou = True
        continue
    io.open(p, "w", encoding="utf-8").write(orig.replace(de, para, 1))
    faltas, _, _ = T.checar(base)
    io.open(p, "w", encoding="utf-8").write(orig)
    marca = nome.split()[0]
    pegou = [x for x in faltas if "[%s]" % marca in x]
    print("%-18s %s  (%d divergencia(s))" % (nome, "PEGOU" if pegou else "PASSOU BATIDO", len(faltas)))
    for x in faltas:
        print("      " + x)
    if not pegou:
        falhou = True

f, t, c = T.checar(base)
print()
print("copia restaurada: %d tabelas, %d celulas, %d divergencias" % (t, c, len(f)))
shutil.rmtree(base)
sys.exit(1 if falhou or f else 0)
