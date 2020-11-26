from django.urls import path
from django.conf.urls import url 
from .views import UserRegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path('register/', UserRegisterView.as_view(), name='register'),

    

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
    name="reset_password"),
    
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
    name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
    name="password_reset_confirm"),

    path('reset/done/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
    name="password_reset_complete"),
]