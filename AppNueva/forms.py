from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    comision = forms.IntegerField()

    

class Buscar(forms.Form):
    comision = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDITAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}