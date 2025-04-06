from http import HTTPStatus

from fastapi.testclient import TestClient

from todolist_fastapi.app import app

cliente = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    resposta = cliente.get('/')

    assert resposta.status_code == HTTPStatus.OK
    assert resposta.json() == {'mensagem': 'Olá Mundo!'}
