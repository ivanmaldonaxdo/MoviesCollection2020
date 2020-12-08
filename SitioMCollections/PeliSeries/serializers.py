from .models import Peliserie, Categoria
from rest_framework import serializers



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        exclude = ['id']

class ProductoSerializer(serializers.ModelSerializer):
    publicado_por = serializers.CharField(read_only=True, source="admin.username")
    fecha_posteo = serializers.CharField(read_only=True, source ="published_date")
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    class Meta:
        model = Peliserie
        exclude = ['published_date']     
    
    

