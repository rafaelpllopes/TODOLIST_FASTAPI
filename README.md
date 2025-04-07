# To Do List
Será criado uma aplicação simples de gerenciamento de tarefas (To-Do List). A aplicação deve permitir que os usuários criem, leiam, atualizem e excluam tarefas.

## Ambiente de Desenvolvimento

- Ubuntu
- Python 3.12
- Docker
- Docker Compose
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
- docker compose up db
- task run (Rodar em modo dev o FastAPI)
- task test (Rodar os testes unitarios)
- task format (Realizar organizar o codigo)

#### Endpoints Dev
- API: http://127.0.0.1:8000
- Docs:
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc

## Backend
O Backend foi utlizado o FastAPI, onde foi utlizado o ORM sqlalchemy, para conexão com o banco de dados, e criado o CRUD.
Também foi criados os testes unitarios, na pasta tests.

```
└── todolist_fastapi (Backend)
    ├── app.py
    └── __init__.py
```

```
├── tests
│   ├── __init__.py
│   └── test_app.py
```


## Frontend
O frontend foi feito sem framework, somente com html, css e js, a comunicação com a API foi utilizado fetch em modo assíncrono.
O frontend em produção irá subir em um servidor nginx pelo docker, rodando na porta 8080.

```
frontend
├── index.html
├── nginx.conf
├── script.js
└── style.css
```

## Em Produção
Para rodar em produção é necessario possuir o Docker, Docker Compose, clonar o projeto.

- ```docker compose up```
### Endpoint
- Pagina principal do To Do List: http://localhost:8080
- Docs:
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc
