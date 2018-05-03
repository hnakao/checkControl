# accounts/forms.py
from django import forms
from django.contrib.auth.models import User

from dashboard.models import PayCheck, Bank


class RegistroUserForm(forms.Form):
    username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Usuario'}, ))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellidos'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repetir la Contraseña'}))

    # photo = forms.ImageField(required=False)
    # ediciones = forms.ModelMultipleChoiceField(queryset=Edicion.objects.all())

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return email

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2


class EditarEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        return super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Comprobar si ha cambiado el email
        actual_email = self.request.user.email
        username = self.request.user.username
        if email != actual_email:
            # Si lo ha cambiado, comprobar que no exista en la db.
            # Exluye el usuario actual.
            existe = User.objects.filter(email=email).exclude(username=username)
            if existe:
                raise forms.ValidationError('Ya existe un email igual en la db.')
        return email


class EditarContrasenaForm(forms.Form):
    actual_password = forms.CharField(label='Contraseña actual', min_length=5,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Nueva contraseña', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir contraseña', min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2


class Forgot_Password_Form(forms.Form):
    email = forms.EmailField(label='E-Mail', required=True, max_length=64,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))


class Recovery_Password_Form(forms.Form):
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                   required=True)
    new_password_2 = forms.CharField(label='Repeat New Password',
                                     widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)


class PayCheckForm(forms.Form):
    bank = forms.ModelChoiceField(queryset=Bank.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'form-control selectpicker', 'style': 'width:480px'}))

    # photo = forms.ImageField(required=False)
    # ediciones = forms.ModelMultipleChoiceField(queryset=Edicion.objects.all())


