# 🎯 Demos - Demonstrações do Sistema

Scripts de demonstração interativa do sistema de validação e recomendação de tags.

## Ficheiros

- `demo.py` - Demo interativa com 2 exemplos
- `DEMO-SAMPLE.md` - Ficheiro com tags válidas
- `DEMO-README.md` - Documentação completa
- `SISTEMA-FUNCIONANDO.txt` - Resumo visual do sistema

## Como Usar

```bash
cd ..
make demo

# Ou diretamente:
python3 demos/demo.py
```

## O que Demonstra

### Demo 1: Ficheiro COM Tags Válidas
- Validação de tags existentes
- Detecção de problemas (se houver)
- Recomendações de tags adicionais

### Demo 2: Ficheiro SEM Tags
- Análise automática de conteúdo
- Recomendações baseadas em keywords
- Cálculo de confidence scores

## Saída Esperada

```
📄 DEMO 1: Ficheiro COM Tags Válidas
✅ Tags encontradas: 6
✓ Nenhum problema encontrado
💡 Recomendações: 8 tags sugeridas

📄 DEMO 2: Ficheiro SEM Tags
⚠️ Nenhuma tag encontrada
💡 Recomendações: 8 tags sugeridas
```

---

Para mais informações: `DEMO-README.md`
