import os
import re
import unicodedata
import sys
import argparse
from pathlib import Path

def normalizar_texto(texto):
    # Remove pontuação, acentos, substitui espaços/hífens por _
    texto = re.sub(r"[^\w\s-]", "", texto)
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    texto = texto.lower().replace(" ", "_").replace("-", "_")
    texto = re.sub(r"^_+", "", texto)  # Remove underscores iniciais
    return texto

def caminho_limpo(path, id_ficheiro):
    partes = list(path.parts)
    if partes[-1].endswith('.md'):
        partes = partes[:-1]
    # Remove prefixo NN- dos diretórios
    partes = [re.sub(r"^\d{2,}-", "", p) for p in partes]
    partes.append(id_ficheiro)
    return partes

def extrair_id(ficheiro):
    with open(ficheiro, encoding="utf-8") as f:
        for _ in range(20):
            linha = f.readline()
            if not linha:
                break
            if linha.startswith("id:"):
                return linha.strip().split(":", 1)[1].strip()
    return None

def limpar_anchors(linha):
    # Remove todos os anchors markdown do tipo {...} no fim da linha (ou no meio, só mantém heading puro)
    return re.sub(r'(\s*\{[^{}]*\})+', '', linha).strip()

def processar_ficheiro(f, docs_root):
    linhas = Path(f).read_text(encoding="utf-8").splitlines()
    novo_conteudo = []
    id_ficheiro = extrair_id(f)
    if id_ficheiro is None:
        print(f"WARNING: Não foi possível extrair o ID do ficheiro {f}. Pulando...")
        return
    
    path = Path(f).resolve()
    rel = path.relative_to(docs_root.resolve())
    caminho = caminho_limpo(rel, id_ficheiro)
   
    base = ":".join(caminho)
    for linha in linhas:
        if linha.strip().startswith("#"):
            # Limpa TODOS os anchors anteriores
            linha_sem_ancora = limpar_anchors(linha)
            heading = re.match(r"^(#{1,6})\s+(.*)$", linha_sem_ancora)
            if heading:
                hashes, titulo = heading.groups()
                sufixo = normalizar_texto(titulo)
                if hashes == "#":
                    anchor_global = f"{base}"
                else:
                    anchor_global = f"{base}#{sufixo}"
                # Adiciona SÓ UM anchor editorial
                linha_com_ancora = f"{linha_sem_ancora} {{{anchor_global}}}"
                novo_conteudo.append(linha_com_ancora)
                continue
        novo_conteudo.append(linha)
    Path(f).write_text("\n".join(novo_conteudo) + "\n", encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adiciona âncoras normalizadas aos ficheiros .md do manual SbD-ToE")
    parser.add_argument("docs_root", type=str, help="Diretório base dos documentos markdown")
    args = parser.parse_args()
    DOCS_ROOT = Path(args.docs_root)
    print("docs_root:", DOCS_ROOT)
    for ficheiro in DOCS_ROOT.rglob("*.md"):
        print(f"Processando: {ficheiro}")
        if ficheiro.name.startswith("_") or ficheiro.name.startswith("README"):
            print("skipping README or hidden file:", ficheiro)
            continue
        
        processar_ficheiro(ficheiro, DOCS_ROOT)
