from typing import List
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from apps.documents.models import DocumentModel

from .serializer import DocumentSerializer, DocumentAPISerializer
from .service import DocumentsService

_SERVICE = DocumentsService()

#bridge entre frontend e backend
def home(request):
    if request.POST:
        if request.POST['action'] == "Adicionar":
            return render_home_create(request)
        elif request.POST['action'] == "Excluir":
            return render_home_delete(request)

    return render_home_find(request, request.POST.get('cpf_cnpj'))


def person_page(request, id: int):
    document = _SERVICE.buscar_document_by_id(id)
    if request.POST:
        serializer = DocumentSerializer(instance=document, data=request.POST, partial=True)
        if not serializer.is_valid():
            messages.error(request, _SERVICE.criar_mensagem_error(serializer.errors))
        else:
            serializer.save()
            messages.success(request, "Dados Editados com sucesso")
            return HttpResponseRedirect('/')
    return render(request, "person.html", context={"document":document})


def render_home(request, documents: List[DocumentModel] = None):
    if documents is None:
        documents = _SERVICE.get_all_documents()
    paginator = Paginator(documents, 5)
    page = request.GET.get('p')
    documents = paginator.get_page(page)
    return render(request, "dash.html", context={"documents": documents})


def render_home_create(request):
    if not _SERVICE.cpf_cnpj_is_valid(request.POST.get("cpf_cnpj")):
        messages.error(request, 'Campo CPF/CNPJ é inválido')
    else:
        data = _SERVICE.criar_data_para_salvar(request.POST)
        serializer = DocumentSerializer(data=data)
        if not serializer.is_valid():
            messages.error(
                request, _SERVICE.criar_mensagem_error(serializer.errors))
        else:
            serializer.save()
            messages.success(request, 'Registro Salvo com Sucesso')

    return render_home(request)


def render_home_delete(request):
    _SERVICE.delete_by_id(request.POST and request.POST['id'])
    messages.info(request, 'Registro Excluido com sucesso')
    return render_home(request)


def render_home_find(request, cpf_cnpj: str):
    documents = None
    if cpf_cnpj is not None:
        documents = _SERVICE.find_documents_by_termo(
            request.POST)
    return render_home(request, documents)


class DocumentsView(viewsets.ModelViewSet):
    serializer_class = DocumentAPISerializer
    queryset = DocumentModel.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "cpf_cnpj",
    )

