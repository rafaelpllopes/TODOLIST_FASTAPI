import os
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    create_engine,
    func,
)
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# Recupera a string de conexão do ambiente
DATABASE_URL = os.getenv(
    'DB_URL', 'mysql+pymysql://user:password@localhost/todo_db'
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# CORS
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# Model
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )


Base.metadata.create_all(bind=engine)


# Schemas
class CriarTafefa(BaseModel):
    title: str


class AtualizarTarefa(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


class ExibirTarefas(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True


def conexao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoints
@app.get('/tarefas', response_model=List[ExibirTarefas])
def exibir_tarefas(db: Session = Depends(conexao_db)):
    """
    Exibi todos as tarefas do banco de dados.
    """
    return db.query(Task).all()


@app.post('/tarefas', response_model=ExibirTarefas)
def criar_tarefa(task: CriarTafefa, db: Session = Depends(conexao_db)):
    """
    Cria uma tarefa nova.
    """
    if not task.title.strip():
        raise HTTPException(status_code=400, detail='Titulo é obrigatorio')
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.put('/tarefas/{tarefa_id}', response_model=ExibirTarefas)
def atualizar_tarefa(
    tarefa_id: int, task: AtualizarTarefa, db: Session = Depends(conexao_db)
):
    """
    Altera o estado da tarefa para concluida ou reabre.
    """
    db_task = db.query(Task).filter(Task.id == tarefa_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    if task.title is not None:
        db_task.title = task.title
    if task.completed is not None:
        db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    return db_task


@app.delete('/tarefas/{tarefa_id}')
def deletar_tarefa(tarefa_id: int, db: Session = Depends(conexao_db)):
    """
    Deleta uma tarefa.
    """
    db_task = db.query(Task).filter(Task.id == tarefa_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    db.delete(db_task)
    db.commit()
    return {'message': 'Tarefa deletada com sucesso'}
