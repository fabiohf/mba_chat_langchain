# Desafio MBA Engenharia de Software com IA - Full Cycle

## Como executar a solução

### 1. Pré-requisitos

- Python 3.11+
- Docker e Docker Compose
- Chave de API da OpenAI

### 2. Clone o repositório

```sh
git clone https://github.com/fabiohf/mba_chat_langchain.git
cd mba_chat_langchain
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
OPENAI_API_KEY=<sua-chave-openai>
OPENAI_MODEL=text-embedding-3-small
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=gpt5_collection
PDF_PATH=./document.pdf
```

> **Atenção:** Ajuste o caminho do `PDF_PATH` se necessário.

### 4. Suba o banco de dados PostgreSQL com extensão pgvector

```sh
docker-compose up -d
```

Aguarde até que o banco esteja pronto.

### 5. Instale as dependências Python

```sh
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
```

### 6. Ingestão do PDF

Execute o script para processar e indexar o PDF:

```sh
python src/ingest.py
```

### 7. Inicie o chat

```sh
python src/chat.py
```

Digite sua pergunta no terminal. Para sair, digite `sair`.

---