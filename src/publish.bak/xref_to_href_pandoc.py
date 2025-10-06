import re
import sys
from pathlib import Path

import re
import emoji

def remover_emojis(texto):
    return emoji.replace_emoji(texto, "")

def remover_todas_ancoras(texto):
    # Remove qualquer {…} que não seja uma anchor LaTeX padrão {#id}
    # Ou seja, remove qualquer {…} que não comece por #
    return re.sub(r'\s*\{(?!#)[^{}]*\}', '', texto)

def filtrar_anchors_pdf(texto):
    return re.sub(
        r'\{([a-zA-Z0-9:_\-]+)#([a-zA-Z0-9_\-]+)\}',
        lambda m: f'{{#{m.group(1).replace(":", "_")}_{m.group(2)}}}',
        texto
    )

def converter_xrefs_para_latex(texto):
    def substituir(match):
        texto_link = match.group(1)
        referencia = match.group(2)
        if "#" in referencia:
            caminho, ancora = referencia.split("#", 1)
        else:
            caminho, ancora = referencia, None

        label = caminho.replace(":", "_")
        if ancora:
            label = f"{label}_{ancora.lstrip('_')}"

        return f"\\hyperref[{label}]{{{texto_link}}}"
    return re.sub(r"\[([^\]]+)\]\(xref:([a-zA-Z0-9:_\-#]+)\)", substituir, texto)

def processar_ficheiros(docs_root):
    for ficheiro in Path(docs_root).rglob("*.md"):
        if ficheiro.name.startswith("_") or ficheiro.name.startswith("README"):
            continue
        conteudo = ficheiro.read_text(encoding="utf-8")
        conteudo = filtrar_anchors_pdf(conteudo)
        conteudo = remover_todas_ancoras(conteudo) 
        conteudo = converter_xrefs_para_latex(conteudo)
        conteudo = remover_emojis(conteudo)
        ficheiro.write_text(conteudo, encoding="utf-8")

if __name__ == "__main__":
    docs_root = sys.argv[1] if len(sys.argv) > 1 else "docs"
    processar_ficheiros(docs_root)
