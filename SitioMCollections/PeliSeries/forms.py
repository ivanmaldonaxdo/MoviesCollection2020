from django import forms
from .models import Peliserie,Carousel,Consulta

class FormPeliserie(forms.ModelForm):
    class Meta:
        model=Peliserie
        fields=['categoria','titulo','autor','reparto','descripcion','genero','year_estreno','caratula']
        widgets ={
            'categoria':forms.Select(attrs={'class': 'form-input'}),
            'titulo':forms.TextInput(attrs={'class': 'form-input'}),
            'autor':forms.TextInput (attrs={'class': 'form-input'}),
            'reparto':forms.TextInput (attrs={'class': 'form-input'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-textarea'}),
            'genero':forms.TextInput(attrs={'class': 'form-input'}),
            'year_estreno':forms.NumberInput(attrs={'class': 'form-input'}),
            'caratula':forms.FileInput(attrs={'class': 'form-input','name':'imagen'})
        }

class FormCarrousel(forms.ModelForm):
    class Meta:
        model=Carousel
        fields=['peliserie','categoria','enunciado','visible','img_carousel']
        widgets ={
            'peliserie':forms.Select(attrs={'class': 'form-input'}),
            'categoria':forms.Select(attrs={'class': 'form-input'}),
            'enunciado':forms.Textarea(attrs={'class': 'form-textarea'}),
            'visible':forms.CheckboxInput(attrs={'class': 'form-input'}),
            'img_carousel':forms.FileInput(attrs={'class': 'form-input'})
        }   


class FormConsulta(forms.ModelForm):
    
    nombre =forms.CharField(min_length=2,max_length=20,
         widget=forms.TextInput(attrs={'class': 'form-input'}))
    correo =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
    motivo =forms.CharField(min_length=4,max_length=15,
         widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    

    class Meta:
        model = Consulta
        fields  = ['nombre', 'fecha', 'correo', 'motivo', 'consulta']
        widgets = {
            
            # 'nombre' :  forms.TextInput(attrs={'class': 'form-input'}),
            'fecha' :  forms.DateInput(attrs={'class': 'form-input'}),
            # 'correo' :  forms.EmailInput(attrs={'class': 'form-input'}),
            # 'motivo' :  forms.TextInput(attrs={'class': 'form-input'}),
            'consulta' :  forms.Textarea(attrs={'class': 'form-textarea'})

        }