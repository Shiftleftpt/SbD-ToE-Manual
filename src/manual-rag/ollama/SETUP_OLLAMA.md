# Setup Ollama para Tagging Tools

## Pré-requisitos

- macOS 11 (Big Sur) ou mais recente
- ~10GB de espaço livre em disco
- RAM: pelo menos 8GB (recomendado 16GB+)

## Instalação do Ollama

### Opção 1: Instalador dmg (Recomendado)

1. **Download**:
   ```bash
   # Visita https://ollama.ai e faz download para Mac
   # ou via curl:
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Verifica instalação**:
   ```bash
   which ollama
   ollama --version
   ```

### Opção 2: Homebrew

```bash
brew install ollama
```

## Download do Modelo Mistral

Depois de instalar Ollama:

```bash
# Baixa o modelo Mistral (vai levar alguns minutos)
ollama pull mistral
```

Verifica se foi baixado:
```bash
ollama list
```

Deverá mostrar algo como:
```
NAME                   ID              SIZE     MODIFIED
mistral:latest         2dfb7e853522    4.1GB    2 minutes ago
```

## Iniciar Ollama Server

### Terminal 1 - Inicia o servidor:
```bash
ollama serve
```

Deverá aparecer algo como:
```
2024/11/23 12:34:56 "POST /api/generate HTTP/1.1" 200 456
```

### Terminal 2 - Roda o script de tagging:
```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/manual-rag

# Ativa venv
source rag_env/bin/activate

# Roda o script
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15 --max-docs 5
```

## Teste Rápido

Se Ollama estiver rodando, teste a conexão:

```bash
curl -X POST http://localhost:11434/api/generate \
  -d '{"model":"mistral","prompt":"Hello","stream":false}'
```

## Performance

- **Primeira execução**: ~15-30s por documento (Mistral aquece)
- **Seguintes**: ~5-10s por documento
- **RAM usada**: ~4GB para Mistral

## Troubleshooting

### "Connection refused on localhost:11434"
- Verifica se `ollama serve` está rodando em outro terminal
- Verifica firewall/proxy settings

### "Model 'mistral' not found"
- Executa `ollama pull mistral`
- Espera o download completar

### Memória insuficiente
- Fecha outras aplicações
- Ou usa modelo menor: `ollama pull neural-chat` (mais leve)

## Alternativa: Sem Ollama (Local Analysis)

O script `suggest_tags.py` tem fallback automático para análise local se Ollama não estiver disponível.

Roda sem Ollama:
```bash
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15
```

(Usa keyword extraction local, menos sofisticado mas funcional)
