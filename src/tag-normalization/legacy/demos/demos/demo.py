#!/usr/bin/env python3
"""
Demo: Sistema de Validação e Recomendação de Tags
Mostra como o sistema funciona com ficheiros reais
"""

import sys
import os
from pathlib import Path

# Setup paths - go up one level to parent directory
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
os.chdir(parent_dir)

from tag_system.core.canonical_tags import CanonicalTagsManager
from tag_system.validators.validation_engine import ValidationEngine
from tag_system.recommenders.recommendation_engine import RecommendationEngine

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def demo_file(file_path, base_path=None):
    """Demo validation and recommendations for a single file"""
    
    if not Path(file_path).exists():
        print(f"❌ Ficheiro não encontrado: {file_path}")
        return
    
    print(f"📄 Ficheiro: {file_path}")
    print(f"{'─'*70}")
    
    # Read file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Show first 400 chars of content
    print("\n📝 CONTEÚDO (primeiras 400 chars):")
    preview = content[:400].replace('\n', '\n    ')
    print(preview)
    
    print(f"\n{'─'*70}\n")
    
    # Initialize engines
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    recommender = RecommendationEngine(canonical_mgr)
    
    # ==================== VALIDAÇÃO ====================
    print_section("1️⃣  VALIDAÇÃO - Tags Existentes")
    
    result = validator.validate_file(file_path)
    
    # Extract frontmatter tags
    frontmatter_tags = result.existing_tags
    
    if frontmatter_tags:
        print(f"✅ Tags encontradas no ficheiro ({len(frontmatter_tags)}):")
        for tag in frontmatter_tags:
            print(f"   • {tag}")
    else:
        print("⚠️  Nenhuma tag encontrada no ficheiro")
    
    # Show validation issues
    if result.issues:
        print(f"\n❌ PROBLEMAS ENCONTRADOS ({len(result.issues)}):\n")
        for issue in result.issues:
            print(f"   [{issue.severity}] {issue.issue_type}")
            print(f"   Tag: {issue.tag}")
            if issue.suggestion:
                print(f"   💡 Sugestão: {issue.suggestion}")
            print()
    else:
        print("\n✓ Nenhum problema encontrado - todas as tags são válidas!")
    
    # ==================== RECOMENDAÇÕES ====================
    print_section("2️⃣  RECOMENDAÇÕES - Tags Sugeridas")
    
    recommendations = recommender.recommend_tags(file_path, min_confidence=0.6, max_recommendations=8)
    
    if recommendations:
        print(f"💡 {len(recommendations)} tag(s) recomendada(s):\n")
        
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec.tag}")
            print(f"      Confiança: {rec.confidence:.1%}")
            print(f"      Razão: {rec.reason}")
            
            # Check for aliases
            canonical_tag = canonical_mgr.get_tag(rec.tag)
            if canonical_tag and canonical_tag.aliases:
                print(f"      Aliases: {', '.join(canonical_tag.aliases[:2])}")
            print()
    else:
        print("ℹ️  Nenhuma recomendação com confiança > 60%")
    
    # ==================== ANÁLISE SEMÂNTICA ====================
    print_section("3️⃣  ANÁLISE SEMÂNTICA - Relações entre Tags")
    
    print("Tags existentes com relações semânticas:\n")
    
    if frontmatter_tags:
        for tag in frontmatter_tags:
            tag_str = str(tag) if not isinstance(tag, str) else tag
            related = canonical_mgr.get_related_tags(tag_str)
            if related:
                print(f"   📌 {tag_str}")
                for related_tag, relation_type in related.items():
                    print(f"      ↔ {related_tag} ({relation_type})")
                print()
    else:
        print("   (Sem tags existentes para análise semântica)")
    
    # ==================== RESUMO ====================
    print_section("4️⃣  RESUMO")
    
    print(f"Tags válidas:        {len(frontmatter_tags)}")
    print(f"Problemas detectados: {len(result.issues)}")
    print(f"Recomendações:       {len(recommendations)}")
    
    if result.issues:
        error_count = sum(1 for i in result.issues if i.severity == "ERROR")
        warning_count = sum(1 for i in result.issues if i.severity == "WARNING")
        print(f"  → Erros: {error_count}")
        print(f"  → Avisos: {warning_count}")


def find_sample_files(base_path, limit=3):
    """Find sample markdown files to demo"""
    md_files = list(Path(base_path).rglob("*.md"))
    # Filter out review files
    md_files = [f for f in md_files if not str(f).endswith('.2review')]
    return md_files[:limit]


def create_demo_without_tags():
    """Create a demo file without tags to show recommendations"""
    demo_content = """---
id: demo-no-tags
title: "Demo Arquivo SEM Tags - Teste de Recomendações"
description: "Ficheiro de demonstração para testar recomendações automáticas de tags"
sidebar_position: 998
---

# Demonstração: Recomendações Automáticas

## Analisando o Conteúdo

Este ficheiro não tem tags definidas. O sistema vai analisar:

1. O título e descrição
2. O conteúdo do documento
3. Contexto de ficheiros relacionados

E vai recomendar tags automáticamente!

## CI/CD Pipeline Seguro

A integração contínua é essencial para segurança. O pipeline deve:

- Executar testes de segurança (SAST)
- Validar dependências (SBOM)
- Escanear vulnerabilidades
- Verificar conformidade
- Registar todas as alterações

## Análise de Dependências

Software Bill of Materials (SBOM) permite:

- Rastrear todas as dependências
- Identificar vulnerabilidades
- Auditar supply chain
- Validar licenças
- Monitorizar atualizações

## Design Seguro

A arquitetura deve considerar:

- Threat modeling desde o início
- Princípios de defesa em profundidade
- Validação de entrada
- Controlo de acesso
- Encriptação de dados

## Testing de Segurança

Diferentes tipos de testes:

- SAST: Análise estática
- DAST: Testes dinâmicos
- Pen testing: Testes penetração
- Fuzzing: Testes com dados aleatórios
"""
    return Path(__file__).parent / "DEMO-NO-TAGS.md", demo_content


if __name__ == "__main__":
    
    print("\n" + "="*70)
    print("  🎯 SISTEMA DE VALIDAÇÃO E RECOMENDAÇÃO DE TAGS - DEMONSTRAÇÃO")
    print("="*70)
    
    # Demo 1: File WITH valid tags
    print("\n" + "─"*70)
    print("📌 DEMO 1: Ficheiro COM Tags Válidas")
    print("─"*70)
    demo_file_path = Path(__file__).parent / "DEMO-SAMPLE.md"
    if demo_file_path.exists():
        demo_file(str(demo_file_path))
    
    # Demo 2: File WITHOUT tags (to show recommendations)
    print("\n" + "─"*70)
    print("📌 DEMO 2: Ficheiro SEM Tags (Recomendações Automáticas)")
    print("─"*70)
    demo_path, demo_content = create_demo_without_tags()
    demo_path.write_text(demo_content, encoding='utf-8')
    demo_file(str(demo_path))
    
    # Cleanup
    try:
        demo_path.unlink()
    except:
        pass
    
    print("\n" + "="*70)
    print("  ✅ Demonstração concluída!")
    print("="*70 + "\n")
