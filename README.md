# To Do List
Será criado uma aplicação simples de gerenciamento de tarefas (To-Do List). A aplicação deve permitir que os usuários criem, leiam, atualizem e excluam tarefas.

## Ambiente de Desenvolvimento

- Ubuntu
- Python 3.12
- Docker
- MariaDB
- Git
- GitHub CLI
- poetry (Gerenciador de dependencias)
- pipx

### Carregar o projeto DEV
Para carregar o projeto para desenvolvimento.

- gh repo clone rafaelpllopes/TODOLIST_FASTAPI
- poetry install
- poetry shell (Entrar no ambiente virtual)
  - pip install "fastapi[standard]" (Talvez precise)
- task run (Rodar em modo dev o FastAPI)
- task test (Rodar os testes unitarios)
- task format (Realizar organizar o codigo)

#### Endpoints
- API: http://127.0.0.1:8000
- Docs:
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc

## Backend
