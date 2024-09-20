from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClienteSignUpForm, MedicoSignUpForm
from .models import Usuario


# Create your views here.
def signup_cliente(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClienteSignUpForm()
    return render(request, 'users/signup_cliente.html', {'form': form})


def signup_medico(request):
    if request.method == 'POST':
        form = MedicoSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = MedicoSignUpForm()
    return render(request, 'users/signup_medico.html', {'form': form})


def login_view(request):
    # Utilize a view de login padrão do Django ou crie sua própria view
    pass
