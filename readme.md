# FastAPI Project

Este repositório contém um projeto de exemplo usando FastAPI, SQLAlchemy e Alembic para migrações, mais um exemplo simples de integração com RabbitMQ (na pasta `RabbitMQ_Example`). O objetivo é servir como ponto de partida para APIs REST leves em Python.

## Conteúdo

- `main.py` - ponto de entrada da aplicação FastAPI.
- `models.py` - modelos SQLAlchemy (tabelas / ORM).
- `schemas.py` - Pydantic schemas (validação/serialização).
- `auth_routes.py` - rotas relacionadas à autenticação (login/registro).
- `order_routes.py` - rotas relacionadas a pedidos (exemplo de funcionalidade).
- `dependencies.py` - dependências do FastAPI (por exemplo: get_db, auth).
- `alembic/` - configuração e scripts de migração do Alembic.
- `requirements.txt` - dependências do Python.
- `RabbitMQ_Example/` - exemplo simples de producer/consumer com RabbitMQ.

## Requisitos

- Python 3.10+ (recomenda-se 3.11)
- PostgreSQL (ou outro banco suportado pelo SQLAlchemy; configure a URI em variáveis de ambiente)
- RabbitMQ (apenas para rodar o exemplo em `RabbitMQ_Example`)

## Instalação (Windows PowerShell)

1. Crie e ative um ambiente virtual:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Atualize pip e instale dependências:

```powershell
python -m pip install --upgrade pip; pip install -r requirements.txt
```

3. Configure variáveis de ambiente necessárias (exemplo):

```powershell
# Exemplo - substitua pelos seus valores
$env:DATABASE_URL = 'postgresql+psycopg2://user:password@localhost:5432/dbname'
$env:SECRET_KEY = 'uma-chavesecreta'
# Caso use RabbitMQ para o exemplo:
$env:RABBITMQ_URL = 'amqp://guest:guest@localhost:5672/'
```

Substitua os valores de exemplo de acordo com seu ambiente.

## Rodando a API localmente

```powershell
# Ative o venv se ainda não estiver ativo
.\.venv\Scripts\Activate.ps1

# Executar com uvicorn (padrão: main:app)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Acesse a documentação interativa em http://127.0.0.1:8000/docs (Swagger UI) ou http://127.0.0.1:8000/redoc.

## Migrações com Alembic

1. Inicialize seu banco de dados conforme a variável `DATABASE_URL`.
2. Gerar uma nova migration após mudanças nos modelos:

```powershell
# Gera uma migration (edite a mensagem conforme necessário)
alembic revision --autogenerate -m "mensagem da migration"

# Aplica as migrations
alembic upgrade head
```

Se houver problemas de importação no `env.py` do Alembic, verifique se o `sys.path` inclui a raiz do projeto ou ajuste as importações conforme necessário.

## RabbitMQ - exemplo

A pasta `RabbitMQ_Example` contém um `producer.py` e `consumer.py` que demonstram um fluxo simples usando pika (ou outra lib compatível). Para testar localmente:

1. Certifique-se que o RabbitMQ está rodando (por exemplo via Docker ou instalação local).
2. Ajuste `RABBITMQ_URL` nas variáveis de ambiente se necessário.
3. Rode o `consumer.py` em um terminal e o `producer.py` em outro.

Exemplo rápido com Docker Compose (na pasta `RabbitMQ_Example` existe um `docker-compose.yml`):

```powershell
# Na pasta RabbitMQ_Example
cd .\RabbitMQ_Example; docker-compose up -d
```

Depois rode os scripts Python:

```powershell
# Terminal 1 - consumer
python .\RabbitMQ_Example\consumer.py

# Terminal 2 - producer
python .\RabbitMQ_Example\producer.py
```

## Testes

Se houver testes (por exemplo `testes.py`), rode com pytest ou diretamente com python:

```powershell
# Usando pytest (se instalado)
pytest -q

# Ou executar script de teste simples
python testes.py
```


