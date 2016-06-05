from django import forms
from .models import Usuario
from django.utils.translation import ugettext_lazy as _

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
            'nombre':_('Nombre de voluntario'),
            'ap_paterno':_('Apellido Paterno'),
            'ap_materno':_('Apellido Materno'),
            'direccion':_('Direccion'),
            'telefono':_('Telefono'),
            'correo':_('Correo electronico'),
            'fecha_nacimiento':_('Fecha de nacimiento'),
            'contrasena':_('Contraseña'),
            'foto':_('Foto'),
            'tipo':_('Tipo de usuario'),
        }
        widgets = {
            'nombre': forms.TextInput(),
            'ap_paterno': forms.TextInput(),
            'ap_materno': forms.TextInput(),
            'direccion': forms.TextInput(),
            'telefono': forms.TextInput(),
            'correo': forms.TextInput(attrs={'type':'email'}),
            'fecha_nacimiento': forms.TextInput(),
            'contrasena': forms.TextInput(attrs={'type':'password'}),
            'tipo': forms.TextInput(attrs={'value':'V','type':'text'}),
        }

class LogForm(forms.Form):
    username = forms.CharField(label='Usurario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
