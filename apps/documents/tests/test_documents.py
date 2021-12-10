import pytest
import json

#Teste get pagina inicial
@pytest.mark.django_db
def test_initial_page(client):

    response = client.get('/')
    assert response.status_code == 200
    
#Teste create pagina inicial
@pytest.mark.django_db
def test_initial_page_create(client):

    data = {
        "cpf_cnpj": "980.680.000-11",
        "nome": "string",
        "endereco": "string",
        "porte": "string",
        "func": "integer",
        "data_inicio": "2021-11-29",
        "data_termino": "2021-11-29",
        "email": "user@example.com",
        "action":"Adicionar"
    }

    response = client.post('/', data=data)
    assert response.status_code == 200

#Teste get list da API
@pytest.mark.django_db
def test_get_documents_list_api(client):

    response = client.get('/api/documents/')

    assert response.status_code == 200
    assert response.json() == []

#Teste create API
@pytest.mark.django_db
def test_create_documents_api(client):
    data = {
        "cpf_cnpj": "980.680.000-11",
        "nome": "string",
        "endereco": "string",
        "porte": "string",
        "func": "10",
        "data_inicio": "2021-11-29",
        "data_termino": "2021-11-29",
        "email": "user@example.com"
    }

    response = client.post('/api/documents/', data=data)

    data_compare = {
        'id': 1,
        'cpf_cnpj': '98068000011',
        'nome': 'string',
        'endereco':'string',
        'porte':'string',
        'func': 10,
        'data_inicio':'2021-11-29',
        'data_termino':'2021-11-29',
        'email': 'user@example.com'
    }

    assert response.status_code == 201
    assert response.json() == data_compare

#Teste validação informações invalidas
@pytest.mark.django_db
def test_create_documents_api_invalid_data(client):
    data = {
       'cpf_cnpj':'string',
        'data_inicio': 'TESTE',
        'data_termino': 'TESTE',
        'email': 'TESTE'
    }

    response = client.post('/api/documents/', data=data)

    data_compare = {
        'nome': ['Este campo é obrigatório.'],
        'data_inicio': ['Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD.'],
        'endereco': ['Este campo é obrigatório.'],
        'func': ['Este campo é obrigatório.'],
        'porte': ['Este campo é obrigatório.'],
        'data_termino': ['Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD.'],
        'email': ['Insira um endereço de email válido.']
    }

    assert response.status_code == 400
    assert response.json() == data_compare

#Teste de id invalido
@pytest.mark.django_db
def test_update_documents_api_invalid_id(client):
    data = {
        'cpf_cnpj': '98068000011',
        'nome': 'string',
        'endereco': 'string',
        'porte': 'string',
        'func': 'integer',
        'data_inicio': '2021-11-29',
        'data_termino': '2021-11-29',
        'email': 'user@example.com'
    }

    response = client.patch('/api/documents/1/', data=data)

    data_compare = {
        "detail": "Não encontrado."
    }

    assert response.status_code == 404
    assert response.json() == data_compare
