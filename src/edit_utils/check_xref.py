import sys
from pathlib import Path
import re
import yaml

def norm(s):
    return (s
            .lower()
            .replace('_', '-')
            .replace('ç', 'c').replace('ã','a').replace('á','a').replace('â','a')
            .replace('é','e').replace('ê','e').replace('í','i').replace('õ','o')
            .replace('ó','o').replace('ú','u').replace('ü','u')
            .replace(' ', '-'))

def fuzzy_match(target, ids):
    t = norm(target.strip('#').strip())
    for k, v in ids.items():
        if t == norm(v):           # match exact id
            return k, v, 'id exato'
        if t in norm(v):           # id contém target
            return k, v, 'id contém target'
        if norm(v) in t:           # target contém id
            return k, v, 'target contém id'
        if t in norm(str(k)):      # path contém target
            return k, v, 'path contém target'
        if norm(str(k)).endswith(t):
            return k, v, 'path termina com target'
    return None, None, 'não encontrado'

def guess_tipo(path):
    if isinstance(path, Path):
        if path.parts[0] == "addon":
            return "addon"
        if path.parts[0] == "canon":
            return "canon"
        if path.name == "intro.md":
            return "intro"
        if path.name == "pre-note.md" or path.name == "pre-intro-rationale.md":
            return "preintro"
        # fallback
        return path.parts[0]
    return "file"

def inventario_ids(md_files, ROOT):
    id_map = {}
    for md in md_files:
        content = md.read_text(encoding='utf-8')
        fm_match = re.match(r'^---(.*?)---', content, re.DOTALL)
        if not fm_match:
            continue
        front = fm_match.group(1)
        try:
            meta = yaml.safe_load(front)
            id_map[md.relative_to(ROOT)] = meta.get('id', md.stem)
        except Exception:
            pass
    return id_map

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 normaliza_links_sbdtoe.py <diretorio_capitulo>")
        sys.exit(1)

    ROOT = Path(sys.argv[1])
    if not ROOT.is_dir():
        print("Diretório não existe:", ROOT)
        sys.exit(2)

    capitulo_base = ROOT.name
    if '-' in capitulo_base:
        capitulo_base = '-'.join(capitulo_base.split('-')[1:])

    md_files = list(ROOT.rglob('*.md'))
    id_map = inventario_ids(md_files, ROOT)

    # Regex para todos os links markdown simples ([texto](alvo))
    regex_global = re.compile(
        r'\[([^\]]+)\]\(([^)]+)\)'
    )

    for md in md_files:
        text = md.read_text(encoding='utf-8')
        changed = False

        def replace_links(match):
            nonlocal changed
            texto = match.group(1)
            destino = match.group(2)
            destino_noprefix = destino.replace('xref:', '').strip()
            # Caso 1: Só âncora (ex: [xxx](#id))
            if destino_noprefix.startswith('#'):
                ancora = destino_noprefix.lstrip('#')
                match_k, match_id, motivo = fuzzy_match(ancora, id_map)
                if match_k:
                    tipo = guess_tipo(match_k)
                    sug = f"xref:sbd-toe:{capitulo_base}:{tipo}:{match_id}"
                    changed = True
                    return f'[{texto}]({sug})'
                else:
                    return f'[{texto}]({destino}) <!-- Precisa revisão manual -->'
            # Caso 2: capNN#alguma-coisa (legacy ou xref:capNN#...)
            elif destino_noprefix.startswith('cap') and '#' in destino_noprefix:
                ancora = destino_noprefix.split('#',1)[1]
                match_k, match_id, motivo = fuzzy_match(ancora, id_map)
                if match_k:
                    tipo = guess_tipo(match_k)
                    sug = f"xref:sbd-toe:{capitulo_base}:{tipo}:{match_id}"
                    changed = True
                    return f'[{texto}]({sug})'
                else:
                    return f'[{texto}]({destino}) <!-- Precisa revisão manual -->'
            # Caso 3: capNN puro (link para intro)
            elif destino_noprefix.startswith('cap'):
                sug = f"xref:sbd-toe:{capitulo_base}:intro"
                changed = True
                return f'[{texto}]({sug})'
            # Caso 4: outros (.md, xref legacy, etc)
            else:
                clean = destino_noprefix.replace('./','').split('#')[0].split(':')[-1]
                ancora = None
                if '#' in destino_noprefix:
                    ancora = destino_noprefix.split('#')[-1]
                match_k, match_id, motivo = fuzzy_match(clean, id_map)
                if match_k:
                    tipo = guess_tipo(match_k)
                    sug = f"xref:sbd-toe:{capitulo_base}:{tipo}:{match_id}"
                    if ancora:
                        sug += f"#{ancora}"
                    changed = True
                    return f'[{texto}]({sug})'
                else:
                    return f'[{texto}]({destino}) <!-- Precisa revisão manual -->'

        new_text = regex_global.sub(replace_links, text)

        if changed:
            md.write_text(new_text, encoding='utf-8')
            print(f'Alterado: {md}')
        else:
            print(f'Sem alterações: {md}')

if __name__ == "__main__":
    main()
