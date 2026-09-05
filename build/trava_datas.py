# -*- coding: utf-8 -*-
"""Trava que impede a data de voltar a ser cravada ou tirada do relogio.

Duas regras, checadas no AST e nao por grep, para nao acusar comentario nem
docstring que apenas MENCIONE o problema:

  1. Nenhum modulo de build/ pode derivar data do relogio.
     Proibido: datetime.now(), datetime.utcnow(), date.today(), time.time(),
     time.localtime(), time.gmtime(), pandas.Timestamp.now().
     Motivo: o gerador roda a cada edicao de texto. Com data de relogio, o
     site passaria a afirmar a cada rebuild que foi conferido hoje, sem que
     ninguem tenha conferido nada.

  2. Nenhum modulo, exceto datas.py, pode escrever a mao AS DATAS DO PROPRIO
     SITE -- o valor de DATA_FONTE e o de DATA_APURACAO. Quem precisa delas
     importa de datas.py.

     A regra e deliberadamente estreita. Data que e CONTEUDO -- quando um
     ensaio comecou, quando a FDA revisou uma bula, quando a WADA passou a
     proibir algo -- e fato reportado, tem que ficar escrita onde esta e nao
     tem nada a ver com esta trava. So a data que o site afirma sobre si
     mesmo e centralizada.

     Docstring de modulo, classe e funcao fica de fora: nao vira HTML.

Roda sozinha (`python build/trava_datas.py`) e tambem no inicio do gerar.py,
que aborta se a trava falhar. Codigo de saida 1 em caso de violacao.
"""
import ast
import glob
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CASA_DA_DATA = "datas.py"   # unico arquivo autorizado a ter data literal

# 1. chamadas de relogio: (objeto, atributo)
RELOGIO = {
    ("datetime", "now"), ("datetime", "utcnow"), ("datetime", "today"),
    ("date", "today"), ("time", "time"), ("time", "localtime"),
    ("time", "gmtime"), ("Timestamp", "now"), ("dt", "now"),
}

# 2. so as datas do proprio site sao proibidas fora de datas.py. Data que e
# conteudo (ensaio, bula, norma) nao entra aqui: e fato reportado.
sys.path.insert(0, AQUI)
from datas import DATA_FONTE, DATA_APURACAO, DATA_MAZDUTIDA  # noqa: E402

DATAS_DA_CASA = {
    "DATA_FONTE": DATA_FONTE,
    "DATA_APURACAO": DATA_APURACAO,
    "DATA_MAZDUTIDA": DATA_MAZDUTIDA,
}


def _docstrings(arvore):
    """Posicoes das docstrings, que nao viram HTML e podem ter data."""
    fora = set()
    for no in ast.walk(arvore):
        if isinstance(no, (ast.Module, ast.ClassDef, ast.FunctionDef,
                           ast.AsyncFunctionDef)):
            corpo = getattr(no, "body", None)
            if corpo and isinstance(corpo[0], ast.Expr) \
                    and isinstance(corpo[0].value, ast.Constant) \
                    and isinstance(corpo[0].value.value, str):
                fora.add(id(corpo[0].value))
    return fora


def checar(diretorio=AQUI):
    faltas = []
    for caminho in sorted(glob.glob(os.path.join(diretorio, "*.py"))):
        nome = os.path.basename(caminho)
        if nome == os.path.basename(__file__):
            continue
        with open(caminho, encoding="utf-8") as f:
            fonte = f.read()
        try:
            arvore = ast.parse(fonte, filename=nome)
        except SyntaxError as e:
            faltas.append(f"{nome}:{e.lineno}: nao compila: {e.msg}")
            continue

        # regra 1 — vale para todo mundo, inclusive datas.py
        for no in ast.walk(arvore):
            if isinstance(no, ast.Call) and isinstance(no.func, ast.Attribute):
                alvo = no.func
                base = alvo.value
                base_nome = getattr(base, "id", None) or getattr(base, "attr", None)
                if (base_nome, alvo.attr) in RELOGIO:
                    faltas.append(
                        f"{nome}:{no.lineno}: data tirada do relogio "
                        f"({base_nome}.{alvo.attr}). A data do site e fato "
                        f"historico — use datas.py.")

        # regra 2 — datas.py e a casa da data
        if nome == CASA_DA_DATA:
            continue
        pular = _docstrings(arvore)
        for no in ast.walk(arvore):
            if isinstance(no, ast.Constant) and isinstance(no.value, str) \
                    and id(no) not in pular:
                for const, valor in DATAS_DA_CASA.items():
                    if valor in no.value:
                        faltas.append(
                            f"{nome}:{no.lineno}: escreveu a mao {valor!r}, "
                            f"que e a data do proprio site. Use "
                            f"`from datas import {const}` e interpole.")
    return faltas


def main():
    faltas = checar()
    if faltas:
        print("TRAVA DE DATAS: %d violacao(oes)\n" % len(faltas), file=sys.stderr)
        for f in faltas:
            print("  " + f, file=sys.stderr)
        print("\nLeia o cabecalho de build/datas.py.", file=sys.stderr)
        return 1
    print("trava de datas: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
