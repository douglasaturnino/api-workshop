import os

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Base
from app.main import app
from app.schema import ProdutosSchema

# Configuração do banco de dados para os testes (forçar a variável de ambiente para 'test')
os.environ["ENV"] = "test"


# Fixture para o cliente de teste
@pytest.fixture(scope="module")
def test_client(db_session):
    """
    Cria uma instância de TestClient que pode ser usada em testes.
    O TestClient é utilizado para simular requisições à API FastAPI.
    """
    with TestClient(app) as client:
        yield client


# Fixture para configurar o banco de dados em memória para os testes
@pytest.fixture(scope="module")
def db_session():
    """
    Fixture que configura e retorna uma sessão de banco de dados para os testes.
    Utiliza um banco SQLite em memória para garantir testes isolados.
    """
    # A URL do banco de dados será automaticamente configurada para o banco SQLite em memória
    DATABASE_URL = "sqlite:///database.db"

    # Criação do engine e da sessão
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Criação das tabelas
    Base.metadata.create_all(bind=engine)

    # Iniciando a sessão
    session = SessionLocal()

    yield session  # Fornece a sessão para os testes

    # Limpeza após os testes
    session.close()
    Base.metadata.drop_all(bind=engine)


# Fixture que cria um produto e retorna o ID para ser utilizado em outros testes
@pytest.fixture(scope="module")
def produto_id(db_session, test_client):
    """
    Cria um produto na API e retorna o ID desse produto.
    Utilizado para testar operações que necessitam de um produto existente.
    """
    produto_data = {
        "id": 1,
        "nome": "Produto Teste",
        "descricao": "Descrição Teste",
        "preco": 19.99,
    }
    # Criando o produto no banco diretamente (simulando a API)
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 201
    return response.json()["id"]


# Teste de listagem de produtos
def test_listar_produtos(db_session, test_client):
    """
    Testa se a rota GET '/produtos' retorna uma lista e um status code 200 (sucesso).
    """
    response = test_client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Teste de inserção de produto
def test_inserir_produto(db_session, test_client):
    """
    Testa a criação de um produto através da rota POST '/produtos'.
    """
    produto_data = {
        "id": 3,
        "nome": "Produto Teste",
        "descricao": "Descrição Teste",
        "preco": 19.99,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == produto_data["nome"]
    assert data["descricao"] == produto_data["descricao"]
    assert data["preco"] == produto_data["preco"]


# Teste de obtenção de um produto
def test_obter_produto(test_client, produto_id):
    """
    Testa a obtenção de um produto específico.
    """
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == produto_id
    assert "nome" in data


# Teste de atualização de um produto
def test_atualizar_produto(test_client, produto_id):
    """
    Testa a atualização de um produto existente.
    """
    novo_dado = {
        "nome": "Produto Atualizado",
        "descricao": "Descrição Atualizada",
        "preco": 29.99,
    }
    response = test_client.put(f"/produtos/{produto_id}", json=novo_dado)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == novo_dado["nome"]


# Teste de remoção de um produto
def test_remover_produto(test_client, produto_id):
    """
    Testa a remoção de um produto.
    """
    response = test_client.delete(f"/produtos/{produto_id}")
    assert response.status_code == 204
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 404


# Teste de modelo de produto válido
def test_modelo_produto_valido():
    produto = ProdutosSchema(
        nome="Teste", descricao="Descrição Teste", preco=10.0
    )
    assert produto.nome == "Teste"
    assert produto.preco == 10.0


# Teste de modelo de produto inválido
def test_modelo_produto_invalido():
    with pytest.raises(ValidationError):
        ProdutosSchema(nome="", preco=-10.0)
