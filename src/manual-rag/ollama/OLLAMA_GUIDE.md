# Ollama - Guia de Instalação e Uso

## O que é Ollama?

**Ollama** é uma ferramenta que permite rodar modelos de linguagem (LLMs) localmente no seu computador, sem precisar de APIs externas ou internet.

- 🏠 **Local-first**: Roda tudo no seu Mac/Linux/Windows
- 🚀 **Rápido**: Baixa latência comparado com APIs cloud
- 🔒 **Privado**: Seus dados nunca saem do seu computador
- 💰 **Grátis**: Código aberto, sem custos
- 📦 **Simples**: Interface de linha de comando intuitiva

## Modelos Disponíveis

Ollama oferece vários modelos prontos para download:

| Modelo | Tamanho | Speed | Qualidade | Ideal para |
|--------|--------|-------|-----------|-----------|
| **Mistral** | 4.1 GB | ⭐⭐⭐ | ⭐⭐⭐⭐ | LLM geral, rápido |
| llama2 | 3.8 GB | ⭐⭐⭐ | ⭐⭐⭐ | LLM geral |
| neural-chat | 4.1 GB | ⭐⭐⭐⭐ | ⭐⭐⭐ | Chat, bem rápido |
| phi | 1.6 GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Rápido, leve |
| orca-mini | 1.3 GB | ⭐⭐⭐⭐⭐ | ⭐⭐ | Ultra leve |

Para o projeto de tagging, usamos **Mistral** (melhor balanço).

## Instalação

### macOS (Recomendado: Homebrew)

```bash
# Instalar Ollama
brew install ollama

# Verificar instalação
ollama --version
```

### macOS (Alternativa: Instalador dmg)

1. Visitar: https://ollama.ai
2. Fazer download do instalador macOS
3. Executar e seguir instruções
4. Após instalar, Ollama fica disponível na linha de comando

### Linux

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Windows

Visitar https://ollama.ai e fazer download do instalador Windows.

## Primeiros Passos

### 1. Baixar um Modelo

```bash
# Baixar Mistral (recomendado para tagging)
ollama pull mistral

# Ou outro modelo
ollama pull llama2
ollama pull neural-chat
```

Isto vai levar alguns minutos (downloads de 1-5 GB).

### 2. Verificar Modelos Instalados

```bash
ollama list
```

Saída esperada:
```
NAME              ID              SIZE      MODIFIED
mistral:latest    2dfb7e853522    4.1GB     2 hours ago
```

### 3. Testar um Modelo Localmente

```bash
# Terminal 1: Iniciar servidor
ollama serve

# Terminal 2: Fazer uma pergunta
ollama run mistral "Olá, como você está?"
```

### 4. Usar via API (para scripts Python)

O servidor Ollama oferece uma API REST:

```bash
# Terminal 1: Iniciar servidor
ollama serve
```

**Endpoint**: `http://localhost:11434`

**Exemplo de uso via curl**:
```bash
curl -X POST http://localhost:11434/api/generate \
  -d '{
    "model": "mistral",
    "prompt": "Explique o que é segurança de software",
    "stream": false
  }'
```

**Exemplo em Python**:
```python
import requests

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'mistral',
        'prompt': 'Olá',
        'stream': False
    }
)

print(response.json()['response'])
```

## Uso para Tagging Tools

### Fluxo Típico

**Terminal 1** - Iniciar servidor Ollama:
```bash
ollama serve
```

Você verá mensagens como:
```
2024/11/23 17:30:45 routes.go:1097: serving on 127.0.0.1:11434
```

**Terminal 2** - Rodar script de tagging:
```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/manual-rag
source rag_env/bin/activate

# Com Ollama rodando, o script usa LLM para análise
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15
```

O script detecta automaticamente se Ollama está rodando:
- ✅ Se disponível: usa Mistral para análise sofisticada
- ⚠️ Se não disponível: usa fallback local (keyword extraction)

## Performance

### Specs Recomendadas

| Métrica | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 8 GB | 16 GB |
| Disco | 10 GB livre | 50 GB livre |
| Processador | Qualquer Apple Silicon / Intel | M1 Pro+ / Ryzen 7+ |

### Tempos de Resposta

Com Mistral em M1 Mac:

- Primeira resposta: ~2-3 segundos (aquecimento)
- Respostas seguintes: ~0.5-1 segundo
- Por documento (tagging): ~5-10 segundos

## Troubleshooting

### "Ollama not found" após instalação

```bash
# Adicionar ao PATH (macOS Homebrew)
export PATH="/usr/local/bin:$PATH"

# Ou verificar instalação
which ollama
```

### "Connection refused on localhost:11434"

```bash
# Ollama não está rodando. Em outro terminal:
ollama serve

# Ou verificar se Ollama está rodando
lsof -i :11434
```

### Memória insuficiente

Se Ollama parar ou ficar muito lento:

1. Fechar outras aplicações (browsers, IDEs, etc.)
2. Usar modelo menor: `ollama pull phi` ou `ollama pull neural-chat`
3. Aumentar RAM disponível

### Modelo não encontrado

```bash
# Listar modelos disponíveis
ollama list

# Se não estiver, baixar
ollama pull mistral
```

## Modelos Alternativos (se Mistral for lento)

### Neural Chat (Mais Rápido)
```bash
ollama pull neural-chat
# Usar em scripts: model="neural-chat"
```

### Phi (Ultra Rápido)
```bash
ollama pull phi
# Tamanho: 1.6 GB
# Velocidade: 2-3x mais rápido que Mistral
# Qualidade: ~80% de Mistral
```

## Comandos Úteis

```bash
# Listar todos os modelos
ollama list

# Remover modelo
ollama rm mistral

# Ver info de um modelo
ollama show mistral

# Rodar modelo interativamente
ollama run mistral

# Ver ajuda
ollama help
```

## Documentação Oficial

- Site: https://ollama.ai
- GitHub: https://github.com/jmorganca/ollama
- Modelos disponíveis: https://ollama.ai/library

## Próximas Ações

1. ✅ Instalar Ollama: `brew install ollama`
2. ✅ Baixar Mistral: `ollama pull mistral`
3. ✅ Testar API: `curl http://localhost:11434/api/tags`
4. ✅ Usar em scripts: ver `rag_tools/tagging_tools/suggest_tags.py`

## Integração com Projeto

O projeto já está configurado para usar Ollama automaticamente:

- **Config**: `src/manual-rag/rag_core/config.py`
- **Endpoint**: `http://localhost:11434`
- **Modelo padrão**: `mistral`
- **Tagging script**: `src/manual-rag/rag_tools/tagging_tools/suggest_tags.py`

Basta iniciar `ollama serve` em um terminal e o script detecta automaticamente! 🚀
