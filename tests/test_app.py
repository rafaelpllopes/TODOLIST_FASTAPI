from http import HTTPStatus

from fastapi.testclient import TestClient

from todolist_fastapi.app import app

client = TestClient(app)


def test_criar_tarefa():
    response = client.post('/tarefas', json={'title': 'Nova tarefa'})
    assert response.status_code == HTTPStatus.OK
    json_data = response.json()
    assert json_data['title'] == 'Nova tarefa'
    assert json_data['completed'] is False
    assert 'id' in json_data


def test_exibir_tarefas():
    response = client.get('/tarefas')
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)


def test_atualizar_tarefa():
    # Criar uma tarefa para ser atualizada
    criar = client.post('/tarefas', json={'title': 'Atualizar tarefa'})
    tarefa_id = criar.json()['id']

    # Atualizar a tarefa
    response = client.put(f'/tarefas/{tarefa_id}', json={'completed': True})
    assert response.status_code == HTTPStatus.OK
    assert response.json()['completed'] is True


def test_deletar_tarefa():
    # Cria tarefa para deletar
    criar = client.post('/tarefas', json={'title': 'Tarefa para deletar'})
    tarefa_id = criar.json()['id']

    # Deleta
    resposta = client.delete(f'/tarefas/{tarefa_id}')
    assert resposta.status_code == HTTPStatus.OK
    assert resposta.json() == {'message': 'Tarefa deletada com sucesso'}

    # Verifica que foi deletado
    resposta = client.get('/tarefas')
    assert all(tarefa['id'] != tarefa_id for tarefa in resposta.json())
