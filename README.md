# Aplicação WEB para cadastro de usuario #

______________________________________________________________________________________________________________________________________________________________________________________
# Primeiro passo #

Na raiz do projeto, rodar o Postgres via comando docker abaixo:

'docker run --name darth-vader-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:10-alpine'

Para parar a docker utilizar o comando abaixo:

'docker stop $(docker ps -aq); docker rm $(docker ps -aq)'
_________________________________________________________________________________________________________________________________________________________________________________
# Segundo passo #

Na raiz do projeto, rodar a maquina virtual python via comando abaixo:

'python -m venv venv'
_________________________________________________________________________________________________________________________________________________________________________________
# Terceiro passo #

Na raiz do projeto, rodar as dependencias do projeto atraves dos comandos abaixo listado no arquivo requirements.txt;
Após isso rodar as migrations.

'venv/Scripts/activate'

'pip install -r requirements.txt'

'python manage.py migrate'
_________________________________________________________________________________________________________________________________________________________________________________
# Quarto passo #

Subir o servidor Python atraves do comando abaixo:

'python manage.py runserver'
_________________________________________________________________________________________________________________________________________________________________________________
# Execução do aplicativo #

Após rodar todas as instancias, no navegador em localHost  127.0.0.1 na porta 8000 acessar a interface do usuario para cadastro de usuarios

' http://127.0.0.1:8000 '
____________________________________________________________________________________________________________________________________________________________________________
# Rota de Suporte #

Atraves da plataforma Swagger foi criado uma rota de suporte para acesso ao projeto. Para acessa-la utilize o caminho abaixo:

' http://127.0.0.1:8000/docs/ '
____________________________________________________________________________________________________________________________________________________________________________
# Testes Unitário #

Foram implementados 06 testes unitarios para a aplicação.

- Teste resposta da pagina inicial

- Teste get list da API

- Teste create API

- Teste validação informações invalidas

- Teste de id invalido

Para rodar os testes unitarios utilize o comando abaixo na raiz do projeto:

'pytest'
____________________________________________________________________________________________________________________________________________________________________________
