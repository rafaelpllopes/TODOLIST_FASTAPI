# Dockerfile

FROM python:3.12-slim

# Instala dependências de sistema
RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do Poetry primeiro (cache eficiente)
COPY pyproject.toml poetry.lock ./
COPY README.md ./README.md

# Copia o restante da aplicação
COPY todolist_fastapi/ ./todolist_fastapi
COPY tests ./tests

# Instala dependências sem criar virtualenvs
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Expõe a porta da aplicação
EXPOSE 5000

# Comando para iniciar o FastAPI com Uvicorn
CMD ["uvicorn", "todolist_fastapi.app:app", "--host", "0.0.0.0", "--port", "5000"]