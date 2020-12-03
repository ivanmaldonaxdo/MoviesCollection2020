from django.db import models
from django.utils import timezone
# import os
# Create your models here.

class Categoria(models.Model):
    nombre_categ=models.CharField(max_length=200,null=False,unique=True,verbose_name='Categoria') 
    def __str__(self): 
        return self.nombre_categ 

class Genero(models.Model):
    descripcion=models.CharField(max_length=200 ,verbose_name='Género') 

    def __str__(self): 
        return self.descripcion     

def ruta_imagen(instance,filename):
    return 'images/{0}/{1}'.format(instance.categoria.nombre_categ, filename)

class Peliserie(models.Model): 
    admin = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name="Admim") 
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    autor=models.CharField(max_length=200,verbose_name="Autor/a",null=True,blank=True) 
    reparto=models.CharField(max_length=200,null=True,blank=True) 
    titulo = models.CharField(max_length=200,verbose_name="Título") 
    descripcion = models.CharField(max_length=1500,verbose_name="Descripción")
    genero=models.CharField(max_length=200 ,verbose_name="Género")
    year_estreno=models.PositiveSmallIntegerField(null=False,verbose_name='Año de Estreno')
    published_date = models.DateTimeField(blank=True, null=True,verbose_name='Fecha de Publicación') 
    caratula=models.ImageField( upload_to=ruta_imagen,null=True,blank=True)
    def publish(self): 
        self.published_date = timezone.now()
        self.save() 

    def __str__(self): 
        return self.titulo
        
def ruta_img_carousel(instance,filename):
    return 'images/carousel/{0}/{1}'.format(instance.categoria.nombre_categ, filename)

class Carousel(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    enunciado = models.CharField(max_length=1500,verbose_name="enunciado",null=True,blank=True)
    peliserie=models.ForeignKey(Peliserie,on_delete=models.CASCADE,null=True,blank=True)
    img_carousel=models.ImageField( upload_to=ruta_img_carousel,null=True,blank=True,verbose_name="imagen")
    fecha_public = models.DateTimeField(blank=True, null=True,verbose_name='Fecha de Publicación') 
    visible=models.BooleanField(blank=True,null=True)
    def publish(self): 
        self.fecha_public = timezone.now()
        self.save() 
        
    def __str__(self): 
        return self.enunciado

class Consulta(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    fecha = models.DateField(default=timezone.now, null=True)
    correo = models.EmailField(null=True)
    motivo = models.CharField(max_length=30, null=True)
    consulta = models.TextField(max_length=200, null=True)
    fecharespuesta=models.DateField(null=True)
    respuesta=models.TextField(max_length=200, null=True)

    

    def __str__(self):
        self.save()
        return self.motivo

       
def img_user(self,filename):       
    return 'images/Usuarios/{0}'.format(filename)

# class Usuario(models.Model):
class Usuario(models.Model):
    nombre=models.CharField(max_length=70,null=False,blank=False)      
    email=models.EmailField(max_length=70,null=False,blank=False)
    contraseña=models.CharField(max_length=8,null=False,blank=False)
    img_usuario=models.ImageField(upload_to=img_user)
    admin = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name="Admim",blank=True, null=True) 
    
    def __str__(self): 
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=150,null=False,blank=False)
    descripcion=models.CharField(max_length=150,null=False,blank=False)   
    fecha_public = models.DateTimeField(blank=True, null=True,verbose_name='Fecha de Publicación') 
    img_notic = models.ImageField(upload_to='images/noticia')
    def publish(self): 
        self.fecha_public = timezone.now()
        self.save()
  
    def __str__(self): 
        return self.titulo
         
