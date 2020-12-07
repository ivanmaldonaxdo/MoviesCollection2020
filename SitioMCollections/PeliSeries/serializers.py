from .models import Peliserie, Categoria
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    categoria_ps = serializers.CharField(read_only=True, source="categoria.nombre_categ")
    id_categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    publicado_por = serializers.CharField(read_only=True, source="admin.username")
    

    class Meta:
        model = Peliserie
        fields = ['categoria_ps','id_categoria','titulo','autor','reparto','descripcion','genero','publicado_por','admin', 'year_estreno','caratula']
        
    def validar_titulo(self, value):
        buscador = Peliserie.objects.filter(titulo=value).exists()

        if buscador:
            raise serializers.ValidationError("Este titulo ya esta registrado")
        return value
    

