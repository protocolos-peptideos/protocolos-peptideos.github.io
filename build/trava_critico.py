"""Trava do CSS critico.

assets/critico-gerado.css e um recorte de assets/estilo.css: as regras que
pegam acima da dobra, extraidas no navegador e postas inline no <head>.

O risco e silencioso. Se alguem edita estilo.css e nao refaz o recorte, o site
continua funcionando, mas a primeira pintura passa a usar um critico velho:
cor errada, cabecalho fora do lugar, e o certo so aparece quando a folha
completa chega. Ninguem percebe olhando a pagina pronta.

Esta trava guarda o sha256 do estilo.css no cabecalho do arquivo gerado e
recusa o build quando os dois saem de sincronia.

Refazer o recorte NAO e automatico: precisa de navegador. O procedimento esta
em assets/critico-gerado.css.
"""
import hashlib
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESTILO = RAIZ / "assets" / "estilo.css"
CRITICO = RAIZ / "assets" / "critico-gerado.css"


def main():
    if not CRITICO.exists():
        sys.exit("trava de critico: assets/critico-gerado.css nao existe")

    # Normaliza CRLF antes de somar. Este repositorio roda com
    # core.autocrlf=true: o git faz checkout do estilo.css com CRLF, e um hash
    # sobre os bytes crus mudaria a cada clone sem que uma linha de CSS
    # mudasse. A trava acusaria um recorte velho que na verdade esta em dia --
    # e o remedio (refazer o recorte) nao arrumaria nada. O .gitattributes ja
    # traz a cicatriz do mesmo problema no shebang do hook.
    atual = hashlib.sha256(ESTILO.read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:16]
    texto = CRITICO.read_text(encoding="utf-8")
    m = re.search(r"estilo\.css sha256\[:16\] = ([0-9a-f]{16})", texto)
    if not m:
        sys.exit("trava de critico: nao achei o hash no cabecalho de critico-gerado.css")
    gravado = m.group(1)

    if atual != gravado:
        sys.exit(
            "trava de critico: estilo.css mudou depois que o critico foi extraido.\n"
            f"  estilo.css agora .......... {atual}\n"
            f"  critico foi feito sobre ... {gravado}\n"
            "  O CSS inline no <head> esta velho. Refaca o recorte no navegador\n"
            "  (procedimento no cabecalho de assets/critico-gerado.css) antes de gerar."
        )

    print(f"trava de critico: ok ({len(texto)} bytes, sobre estilo.css {atual})")


if __name__ == "__main__":
    main()
