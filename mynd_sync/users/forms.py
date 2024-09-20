from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Medico

class ClienteSignUpForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'phone', 'birth', 'CPF', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True
        user.birth = self.cleaned_data.get('birth')
        user.phone = self.cleaned_data.get('phone')
        user.CPF = self.cleaned_data.get('CPF')
        if commit:
            user.save()
        return user

class MedicoSignUpForm(UserCreationForm):
    birth = forms.DateField(required=False)
    phone = forms.CharField(max_length=15, required=False)
    CPF = forms.CharField(max_length=11, required=True)
    DRT = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'phone', 'birth', 'CPF', 'password1', 'password2', 'DRT']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_medico = True
        user.birth = self.cleaned_data.get('birth')
        user.phone = self.cleaned_data.get('phone')
        user.CPF = self.cleaned_data.get('CPF')
        if commit:
            user.save()
            Medico.objects.create(user=user, DRT=self.cleaned_data['DRT'])
        return user
