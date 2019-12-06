from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from cursos.models import Curso

# Create your views here.
def index_page(request):
    '''Carga la landing page para el usuario final'''
    cursos = Curso.objects.all()
    context = {
               'cursos': cursos,
    }
    return render(request, 'frontend/index.html',context)

def inicio(request):
    '''Carga la pagina de administracion despues de login'''
    return render(request, 'backend/index.html')

def login_page(request):
    "Logueamos a un administrador"
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        # Recuperamos los datos
        username  = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # Verificamos credenciales
        user = authenticate(username = username, password = password)

        # Si existe lo Logueamos
        if user is not None and user.groups.filter(name='Administrador').exists():
            print("Login correcto")
            login(request, user)
            return redirect('cursos:curso_list')
        else:
            messages.error(request, 'Credenciales no validas, solo puede ingresar un administrador.')

    return render(request, 'frontend/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('index')
