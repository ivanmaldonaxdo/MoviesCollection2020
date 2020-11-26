from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.urls import reverse_lazy
from usuarios.forms import RegistroUsuario


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegistroUsuario
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


