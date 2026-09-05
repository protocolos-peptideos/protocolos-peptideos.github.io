"""Baixa as fontes do Google e as hospeda no repositorio.

Roda uma vez, quando as fontes mudarem. O resultado dele (assets/fontes/*.woff2
e o bloco @font-face no topo de assets/estilo.css) e versionado, entao o site
no ar nao depende deste script nem do Google.

Subsets mantidos: latin, latin-ext e greek. O greek entra porque o site usa
alfa, beta, gama, delta e kappa em nome de composto (TGF-beta, timosina alfa-1).
Fraunces nao oferece greek e nao precisa: as letras gregas aparecem em corpo de
texto, que e Inter, nao em display.

Os pedidos usam a sintaxe de faixa (400..700) de proposito: o Google devolve
fonte variavel, um arquivo por subset em vez de um por peso, e o eixo opsz da
Fraunces sobrevive. Sem esse eixo o font-optical-sizing: auto do estilo.css
nao teria efeito nenhum.
"""
import re
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "assets" / "fontes"

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

CSS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Fraunces:opsz,wght@9..144,400..700"
    "&family=Inter:wght@400..700"
    "&family=JetBrains+Mono:wght@400..500"
    "&display=swap"
)

SUBSETS_MANTIDOS = {"latin", "latin-ext", "greek"}


def busca(url, binario=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        dados = r.read()
    return dados if binario else dados.decode("utf-8")


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    css = busca(CSS_URL)

    # Cada bloco vem precedido de um comentario com o nome do subset.
    blocos = re.findall(r"/\* (\S+) \*/\s*(@font-face \{.*?\})", css, re.S)
    if not blocos:
        sys.exit("nao achei nenhum @font-face no CSS do Google")

    saida = []
    baixados = 0
    for subset, bloco in blocos:
        if subset not in SUBSETS_MANTIDOS:
            continue
        familia = re.search(r"font-family: '([^']+)'", bloco).group(1)
        url = re.search(r"url\((https://[^)]+)\)", bloco).group(1)
        nome = f"{familia.lower().replace(' ', '-')}-{subset}.woff2"

        alvo = DESTINO / nome
        dados = busca(url, binario=True)
        if not dados.startswith(b"wOF2"):
            sys.exit(f"{nome}: nao veio woff2 (assinatura {dados[:4]!r})")
        alvo.write_bytes(dados)
        baixados += 1
        print(f"  {nome:<34} {len(dados):>7} bytes")

        bloco = bloco.replace(f"url({url})", f"url(fontes/{nome})")
        saida.append(f"/* {subset} */\n{bloco}")

    destino_css = DESTINO.parent / "fontes-gerado.css"
    destino_css.write_text(
        "/* GERADO por build/baixa_fontes.py. Nao editar a mao. */\n\n"
        + "\n".join(saida) + "\n",
        encoding="utf-8", newline="\n")
    print(f"\n{baixados} arquivos em {DESTINO}")
    print(f"blocos @font-face em {destino_css}")


if __name__ == "__main__":
    main()
