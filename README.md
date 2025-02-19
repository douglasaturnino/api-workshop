# Objetivo
O objetivo desse é mostrar como é possível fazer o deploy de vários tipos de produtos de dados, passando desde a etapa de especificação até a fase de deploy.
Fazem parte dessa solução:

[FastAPI](https://github.com/douglasaturnino/api-workshop-fastapi)
[Streamlit](https://github.com/douglasaturnino/api-workshop-streamlit)


[FastAPI](https://api-workshop-yekz.onrender.com/docs)
[Streamlit](https://api-workshop-dso.streamlit.app/)

# Criando nosso ambiente virtual

Ambientes virtuais são uma ferramenta para manter as dependências necessárias para diferentes projetos em locais separados, evitando problemas de compatibilidade. Neste projeto estamos utilizando o como gerenciador de ambiente o [UV da astral](https://docs.astral.sh/uv/getting-started/features/).

```bash
uv sync
```

Com essa comando caso não tenho a versão `3.12.8` instalado o uv irá instalar a versão.

# Ativando nosso ambiente virtual

Para ativar o ambiente virtual utilizando o uv é igual a utilização do pip nesse caso será:

```bash
source .venv/bin/activate
```
# Executando o servidor

Para executar o servidor, precisamos usar o Uvicorn e passar o nome do arquivo e o nome da variável que contém a instância do FastAPI.

```bash
uvicorn app.main:app --reload
```

Como alternativa podemos utilizar o taskipy

```bash
task run
```

# Rodando os testes

Testes automatizados são uma parte importante do desenvolvimento de software. Eles são usados para garantir que o código que escrevemos faça o que esperamos que ele faça.

```bash 
pytest -v
```

Como alternativa podemos utilizar o taskipy

```bash
task test
```
# 

