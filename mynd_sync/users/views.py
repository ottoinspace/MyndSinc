from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ClienteSignUpForm, MedicoSignUpForm
from .models import Usuario
from django.contrib import messages


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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.username}!')
            return redirect('home')  # Redireciona para a página principal ou qualquer outra página
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')
