#!/usr/bin/env python3
import yaml
from pathlib import Path

def parse_book_config(yaml_file):
    with open(yaml_file, 'r') as f:
        book = yaml.safe_load(f)

    chapters = book.get('chapters', [])
    files = []
    for chapter in chapters:
        root = chapter.get('root')
        addons = chapter.get('addon', [])
        if root:
            files.append(f"{root}/intro.md")
        for addon in addons:
            files.append(f"{root}/addon/{addon}")
    return files

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: parse_book_yaml.py book.yaml")
        exit(1)
    files = parse_book_config(sys.argv[1])
    for f in files:
        print(f)
