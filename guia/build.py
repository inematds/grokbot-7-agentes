#!/usr/bin/env python3
"""Monta o guia nos 3 idiomas.

Lê guia/_src/<idioma>.html e troca cada marcador <!--PROMPT:NN--> pela
"Instrução pronta" (o primeiro bloco ```text) da ficha agentes/[<idioma>/]NN-*.md.
Assim a página e as fichas nunca divergem.

Uso: python3 guia/build.py
"""
import glob
import html
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDIOMAS = {
    # idioma: (pasta das fichas, arquivo de saída, botão, botão depois de copiar)
    "pt": ("agentes", "guia/index.html", "Copiar", "Copiado!"),
    "en": ("agentes/en", "guia/en/index.html", "Copy", "Copied!"),
    "es": ("agentes/es", "guia/es/index.html", "Copiar", "¡Copiado!"),
}


def prompt_da_ficha(pasta, nn):
    achados = glob.glob(os.path.join(RAIZ, pasta, f"{nn}-*.md"))
    if len(achados) != 1:
        sys.exit(f"ficha {nn} não encontrada (ou repetida) em {pasta}: {achados}")
    texto = open(achados[0], encoding="utf-8").read()
    m = re.search(r"```text\n(.*?)\n```", texto, re.S)
    if not m:
        sys.exit(f"sem bloco ```text em {achados[0]}")
    return m.group(1)


def main():
    erros = 0
    for idioma, (pasta, saida, botao, ok) in IDIOMAS.items():
        fonte = os.path.join(RAIZ, "guia/_src", f"{idioma}.html")
        if not os.path.exists(fonte):
            print(f"[{idioma}] sem fonte {fonte}, pulando")
            erros += 1
            continue
        pagina = open(fonte, encoding="utf-8").read()

        def troca(m):
            p = html.escape(prompt_da_ficha(pasta, m.group(1)), quote=False)
            return f'<pre>{p}</pre><button class="cp" type="button" data-ok="{ok}">{botao}</button>'

        pagina, n = re.subn(r"<!--PROMPT:(\d\d)-->", troca, pagina)
        destino = os.path.join(RAIZ, saida)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        open(destino, "w", encoding="utf-8").write(pagina)
        print(f"[{idioma}] {saida}: {n} instruções")
        if n != 7:
            erros += 1
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
