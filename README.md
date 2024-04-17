# backend-mvp
# API de Cadastro de Usuários - Projeto PUCRIO

Este é um projeto para cadastro e gerenciamento de usuários, desenvolvido em Python utilizando o framework Flask e integrado a um banco de dados MySQL. Este projeto faz parte do Curso de Pós-graduação em Engenharia de Software do CCE-PUC Rio.

## Como Executar

Para executar este projeto localmente, siga estas instruções:

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Python (versão 3.6 ou superior)
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)
- MySQL Server
- Um navegador da web (como Google Chrome, Mozilla Firefox, etc.)

### Clonar o Repositório

Clone este repositório para o seu ambiente local usando o seguinte comando:
`git clone <URL do repositório>`

## Configurar o Ambiente

Antes de começar, certifique-se de configurar corretamente o ambiente, incluindo a configuração do servidor MySQL e a criação do banco de dados `projeto_crud`. Você pode encontrar as configurações de conexão no código.

## Executar a Aplicação

Para iniciar a aplicação, siga estas etapas:

1. Navegue até a pasta onde o repositório foi clonado.
2. Execute o seguinte comando para iniciar a aplicação:
`python app.py`
A aplicação será iniciada e estará disponível em http://localhost:5000.

## Endpoints
- GET /buscar_usuarios: Retorna a lista de todos os usuários cadastrados.
- POST /cadastrar_usuario: Cadastra um novo usuário.
- GET /buscar_usuario/<id>: Retorna os detalhes de um usuário específico com o ID fornecido.
- DELETE /deletar_usuario/<id>: Deleta um usuário com o ID fornecido.
