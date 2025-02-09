from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200


def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"mensagem": "Olá, mundo!"}


def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200


def test_tamanho_lista_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3


def test_pega_um_produto():
    response = client.get("/produtos/1")
    assert response.status_code == 200


def test_pega_um_produto_json():
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone de última geração",
        "preco": 1500.00,
    }


def test_adicionar_produto():
    response = client.post(
        "/produtos",
        json={
            "id": 5,
            "nome": "Notebook",
            "descricao": "Um notebook de última geração",
            "preco": 2500.00,
        },
    )
    assert response.status_code == 200


def test_adicionar_produto_json():
    response = client.post(
        "/produtos",
        json={
            "id": 5,
            "nome": "Notebook",
            "descricao": "Um notebook de última geração",
            "preco": 2500.00,
        },
    )
    assert response.json() == {
        "id": 5,
        "nome": "Notebook",
        "descricao": "Um notebook de última geração",
        "preco": 2500.00,
    }
