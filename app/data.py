from typing import Dict, List


class Produto:
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um smartphone de última geração",
            "preco": 1500.00,
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um notebook de última geração",
            "preco": 3500.00,
        },
        {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um tablet de última geração",
            "preco": 2000.00,
        },
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagem": "Produto não encontrado."}

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto
