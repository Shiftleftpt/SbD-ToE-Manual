import argparse
import yaml
from pathlib import Path
import re

# ===== FUNÇÕES DOS FILTROS =====

def remover_blocos_print_only(texto):
    return re.sub(
        r'<!--\s*print-only\s*-->(.*?)<!--\s*print-only:end\s*-->',
        '',
        texto,
        flags=re.DOTALL | re.IGNORECASE
    )

def remover_blocos_web_only(texto):
    return re.sub(
        r'<!--\s*web-only\s*-->(.*?)<!--\s*web-only:end\s*-->',
        '',
        texto,
        flags=re.DOTALL | re.IGNORECASE
    )

def remover_emojis(texto):
    try:
        import emoji
        return emoji.replace_emoji(texto, "")
    except ImportError:
        return texto  # fallback: não remove

def remover_todas_ancoras(texto):
    # Remove qualquer {…} que não seja uma anchor LaTeX padrão {#id}
    # Ou seja, remove qualquer {…} que não comece por #
    return re.sub(r'\s*\{(?!#)[^{}]*\}', '', texto)

def filtrar_anchors_pdf(texto):
    # {algo#id}  → {#algo_id}
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

def filtrar_anchors_web(texto):
    # Remove anchors em headings de nível 1 (# ...)
    texto = re.sub(r'^(# .+?)\s*\{[^{}]+\}', r'\1', texto, flags=re.MULTILINE)
    # Para os restantes, converte anchor global para local
    texto = re.sub(
        r'\{([a-zA-Z0-9:_\-]+)#([a-zA-Z0-9_\-]+)\}',
        lambda m: f'{{#{m.group(2)}}}',
        texto
    )
    return texto

def converter_xref_links_web(texto):
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

def remover_separadores(texto):
    # Remove qualquer \n---\n (linha em branco, três traços, linha em branco)
    # exceto o frontmatter inicial
    # Mantém os --- do início do ficheiro (YAML frontmatter)
    if texto.startswith('---'):
        partes = texto.split('---', 2)
        if len(partes) == 3:
            inicio = '---' + partes[1] + '---'
            resto = partes[2]
            novo_resto = re.sub(r'\n\s*---\s*\n', '\n', resto)
            return inicio + novo_resto
    # Para ficheiros sem frontmatter, aplica em tudo
    return re.sub(r'\n\s*---\s*\n', '\n', texto)

# ===== PIPELINE PRINCIPAL =====

def processar_ficheiro(ficheiro, config):
    conteudo = Path(ficheiro).read_text(encoding="utf-8")

    # 1. REMOVER print-only
    if config.get('remove_print_only', False):
        conteudo = remover_blocos_print_only(conteudo)

    # 2. REMOVER web-only
    if config.get('remove_web_only', False):
        conteudo = remover_blocos_web_only(conteudo)

    # 3. PDF-specific transforms
    if config.get('to_pdf', False):
        conteudo = filtrar_anchors_pdf(conteudo)
        conteudo = remover_todas_ancoras(conteudo)
        conteudo = converter_xrefs_para_latex(conteudo)
        if config.get('remove_emojis', False):
            conteudo = remover_emojis(conteudo)

    # 4. WEB-specific transforms
    if config.get('to_web', False):
        conteudo = filtrar_anchors_web(conteudo)
        conteudo = converter_xref_links_web(conteudo)

    Path(ficheiro).write_text(conteudo, encoding="utf-8")
    
    # Remover separadores visuais --- (não frontmatter)
    if config.get('remove_separadores', False):
        conteudo = remover_separadores(conteudo)

# ===== CLI & CONFIG =====

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Super Filtro SbD-ToE (print/web, xref, anchors, etc)")
    parser.add_argument("--inputdir", default="docs", help="Diretório de entrada com ficheiros .md")
    parser.add_argument("--bookyml", default="book.yml", help="Ficheiro book.yml (com bloco 'filters')")
    parser.add_argument("--profile", default="print", choices=["print","web"], help="Perfil de build (print/web)")
    args = parser.parse_args()

    # Ler config do book.yml
    with open(args.bookyml, "r", encoding="utf-8") as f:
        book = yaml.safe_load(f)
    config = book.get("filters", {}).get(args.profile, {})

    # Detalhe do perfil carregado
    print(f"[INFO] Profile ativo: {args.profile} | Config: {config}")

    inputdir = Path(args.inputdir).resolve()
    for ficheiro in inputdir.rglob("*.md"):
        if ficheiro.name.startswith("_") or ficheiro.name.startswith("README"):
            continue
        print(f"[INFO] A processar: {ficheiro}")
        processar_ficheiro(ficheiro, config)
