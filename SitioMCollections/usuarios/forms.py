from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistroUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            
            
            
        ]
        help_texts = {
            'username': None
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-input',
                'placeholder':'Ingrese un nombre de usuario'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-input', 
                'placeholder':'Ingrese su nombre'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-input', 
                'placeholder':'Ingrese su Apellido'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-input',
                'placeholder':'Ingrese un correo valido'}),
        }
        
    def clean(self):
    
        cleaned_data = super(RegistroUsuario, self).clean()

        user_exists = (User.objects.filter(username = cleaned_data.get('username')).count() > 0)

        if user_exists:
            self.add_error('username', 'Ese usuario ya existe')

    
   
        