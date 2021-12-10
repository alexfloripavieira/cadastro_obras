from rest_framework import fields, serializers
from apps.documents.service import DocumentsService
from .models import DocumentModel
_SERVICE = DocumentsService()

#Validações de frontend
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = (
            "id",
            "nome",
            "cpf_cnpj",
            "endereco",
            "porte",
            "func",
            "data_inicio",
            "data_termino",
            "email",
        )
        extra_kwargs = {"username": {"error_messages": {
            "unique": "Registro ja existente"}}}
        error_messages = {"cpf_cnpj": "Registro ja existente"}

    def update(self, instance, validated_data):
        validated_data["cpf_cnpj"] = _SERVICE.clean(validated_data["cpf_cnpj"])
        return super().update(instance, validated_data)

#Validações de backend 
class DocumentAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = (
            "id",
            "nome",
            "cpf_cnpj",
            "endereco",
            "porte",
            "func",
            "data_inicio",
            "data_termino",
            "email",
        )

    def update(self, instance, validated_data):
        if not _SERVICE.cpf_cnpj_is_valid(validated_data["cpf_cnpj"]):
            raise serializers.ValidationError("CPF/CNPJ inválido")
        validated_data["cpf_cnpj"] = _SERVICE.clean(validated_data["cpf_cnpj"])
        return super().update(instance, validated_data)

    def create(self, validated_data):
        if not _SERVICE.cpf_cnpj_is_valid(validated_data["cpf_cnpj"]):
            raise serializers.ValidationError("CPF/CNPJ inválido")
        validated_data["cpf_cnpj"] = _SERVICE.clean(validated_data["cpf_cnpj"])
        return super().create(validated_data)
