# 🚀 Analisador de Logs de Segurança

Ferramenta CLI em Python para análise de logs HTTP com detecção automática de brute force.

# Analisador de Logs - Python

Ferramenta CLI para análise de logs de segurança.

## Funcionalidades
- Contagem de acessos por IP
- Contagem de status HTTP
- Detecção de brute force (401)

## Como usar
1. Baixe o repositório
2. Coloque o arquivo `teste.log` **na mesma pasta** do `analisador_logs.py`
3. Abra o terminal na pasta do projeto
4. Execute:
python analisador_logs.py
5. Digite o caminho do arquivo log: teste.log

## Exemplo de log
192.168.0.10 - - [data] "GET /login" 401

