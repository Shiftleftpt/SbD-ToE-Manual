import argparse
import re
import sys
from pathlib import Path

def filtrar_anchors_web(texto):
    # Remove anchors em headings de nível 1 (# ...)
    print("Filtrando anchors web...")
    texto = re.sub(r'^(# .+?)\s*\{[^{}]+\}', r'\1', texto, flags=re.MULTILINE)
    # Para os restantes, converte anchor global para local
    texto = re.sub(
        r'\{([a-zA-Z0-9:_\-]+)#([a-zA-Z0-9_\-]+)\}',
        lambda m: f'{{#{m.group(2)}}}',
        texto
    )
    return texto


def converter_xref_links(texto):
    # Substitui [texto](xref:cap02:addon:classificacao#matriz_de_classificacao) por [texto](/cap02/addon/classificacao#matriz_de_classificacao)
    print("Convertendo links xref para paths web...")
    def substituir(match):
        texto_link = match.group(1)
        conteudo = match.group(2)
        if "#" in conteudo:
            caminho, ancora = conteudo.split("#", 1)
        else:
            caminho, ancora = conteudo, None
        partes = caminho.split(":")
        caminho_base = "/" + "/".join(partes)
        if ancora:
            caminho_base += f"#{ancora}"
        return f"[{texto_link}]({caminho_base})"
    return re.sub(r"\[([^\]]+)\]\(xref:([a-zA-Z0-9:_\-#]+)\)", substituir, texto)

def processar_ficheiro(ficheiro):
    conteudo = Path(ficheiro).read_text(encoding="utf-8")
    conteudo = filtrar_anchors_web(conteudo)    # só o anchor local
    conteudo = converter_xref_links(conteudo)   # converte xrefs para path web
    Path(ficheiro).write_text(conteudo, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converte xrefs e anchors para paths Docusaurus.")
    parser.add_argument("--inputdir", "--input-dir", dest="inputdir", default="docs",
                        help="Diretório de entrada com ficheiros .md")
    args = parser.parse_args()
    inputdir = Path(args.inputdir).resolve()
    print(f"Converter links xref para paths docusaurus ready nos ficheiros em: {inputdir}")
    for ficheiro in inputdir.rglob("*.md"):
        print(f"converter ancoras editoriais no ficheiro: {ficheiro}")
        if ficheiro.name.startswith("_") or ficheiro.name.startswith("README"):
            continue
        processar_ficheiro(ficheiro)


