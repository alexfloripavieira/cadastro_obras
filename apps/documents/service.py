from typing import List
from pycpfcnpj import cpfcnpj
from .models import DocumentModel
from django.db.models import Q, Value


class DocumentsService():
    def cpf_cnpj_is_valid(self, cpf_cnpj: str) -> bool:
        return cpfcnpj.validate(cpf_cnpj)

    def buscar_document_by_id(self, id: int) -> DocumentModel:
        return DocumentModel.objects.filter(id=id).first()

    def get_all_documents(self) -> List[DocumentModel]:
        return DocumentModel.objects.all().order_by("-id")

    def clean(self, cpf_cnpj: str) -> str:
        return cpf_cnpj.replace("-", "").replace(".", "").replace("/", "").strip()

    def find_documents_by_termo(self, termo: dict) -> List[DocumentModel]:
        nome = termo.get("nome").strip() if termo.get(
            "nome") is not None else ""

        cpf_cnpj = termo.get("cpf_cnpj").strip() if termo.get(
            "cpf_cnpj") is not None else ""

        email = termo.get("email").strip() if termo.get(
            "email") is not None else ""

        data_inicio = None
        if termo.get("data_inicio") is not None and termo.get("data_inicio") != "":
            data_inicio = termo.get("data_inicio").strip()

       

        documents = DocumentModel.objects.filter(
            nome__icontains=nome,
            cpf_cnpj__icontains=cpf_cnpj,
            email__icontains=email,
        )

        if data_inicio is not None:
            documents = documents.filter(data_inicio=data_inicio)

        return documents

    def delete_by_id(self, id: str) -> int:
        return DocumentModel.objects.filter(id=id).delete()

    def criar_data_para_salvar(self, data: dict):
        return {
            "nome": data.get("nome"),
            "cpf_cnpj":  self.clean(data["cpf_cnpj"]),
            "endereco": data.get("endereco"),
            "porte": data.get("porte"),
            "func": data.get("func"),
            "data_inicio": data.get("data_inicio"),
            "data_termino": data.get("data_termino"),
            "email": data.get("email"),
        }

    def criar_mensagem_error(self, errors: dict) -> str:
        message = ""
        for key in errors.keys():
            message += f"{key}: {errors.get(key)[0].title()} \n"
        return message
