from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credenciales inválidas')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo ya está en uso')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'Usuario creado correctamente')
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    logout_user(request)
    return redirect('/')
