from django.contrib import admin
from .models import Categoria,Peliserie,Carousel,Consulta,Noticia,Favorito
# Register your models here.
admin.site.register([Categoria,Peliserie,Carousel, Consulta,Noticia,Favorito])
