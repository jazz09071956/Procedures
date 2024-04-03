from django.shortcuts import render
#from django.contrib.messages.api import success
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
#from django.contrib.auth.models import User
from accounts.models import Usuario
#from datetime import timedelta, datetime
#from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from django.urls import reverse_lazy
#from django.views import generic

from django.views import generic
from io import BytesIO
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from django.utils.dateparse import parse_date
import datetime
from django.http import HttpResponse

# login class-based view
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        # Display the login form
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # Handle form submission for user login
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                messages.success(request, 'Bienvenido, ya has logrado entrar!')
                return redirect('home_view')  # Redirect to the home page or any desired page after login
            else:
                messages.error(request, 'Usuario o Password Incorrecto.')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        # Log the user out
        logout(request)
        messages.success(request, 'Hasta luego, ya has salido de la aplicacion!')
        return redirect('home_view')  # Redirect to the home page or any desired page after login

def index(request):
    return render(request, 'accounts/index.html')
def login1(request):
    if request.method == 'POST':
#        print('Submitted Reg')
#        return redirect('register')
#        return
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Felicidades, ya has ingresado')
            return redirect('index')
        else:
            messages.error(request, 'Credenciales invalidas')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout1(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Ya has salido')
        return redirect('login')

def register(request):
    if request.method == 'POST':
#        print('Submitted Reg')
#        messages.error(request, 'Probando mensajes de error')
#        return redirect('register')
        #obtener valores del formulario
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #chequear si los password coinciden
        if password == password2:
            #verificar el nombre de usuario no este duplicado, objects busca en la base de datos
            if Usuario.objects.filter(username=username).exists():
                messages.error(request, 'Ese nombre de usuario ya esta en uso')
                return redirect('register')
            else:
                if Usuario.objects.filter(email=email).exists():
                    messages.error(request, 'Ese correo ya esta en uso')
                    return redirect('register')
                else:
                    #se ve bien
                    user = Usuario.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #existen dos maneras 1- login after register
                    #auth.login(request, user)
                    #messages.success(request, 'you are now logged in')
                    #return redirect(index)
                    #la otra forma es login manual despues de registrarse
                    user.save()
                    messages.success(request, 'ahora ya estas registrado y puedes ingresar')
                    return redirect('login')
                    
            
        else:
            messages.error(request, 'Los Passwords no coinciden')
            return redirect('register')

#        return
    else:
        return render(request, 'accounts/register.html')


def usuariosaplicacionxls(request):
    context = {
        'archivo': 'UsuariosAplicacion'
    }

    return render(request, 'accounts/usuariosaplicacion.html', {'context': context})


def usuariosaplicacion(request):
    user=request.user
    codigo_sala=user.codigo_sala
    queryset_list = Usuario.objects.values('username','codigo_sala','nombre_sala','password','email','date_joined','is_active').order_by('codigo_sala')

    if not user.is_superuser:
        queryset_list = queryset_list.filter(codigo_sala=codigo_sala).order_by('codigo_sala')

    #contenido del campo archivo
    if 'archivo' in request.GET:
        archivo = request.GET['archivo']


    # Crear un objeto (object) para crear archivos en memoria
    temp_file = BytesIO()

    # Empezar un libro (workbook)
    workbook = xlsxwriter.Workbook(temp_file)
    worksheet = workbook.add_worksheet()
    
    # Prepararar los datos a escribirse
    data = []
    for usuario in queryset_list:
        username=usuario['username']
        codigo_sala=usuario['codigo_sala']
        nombre_sala=usuario['nombre_sala']
        password=usuario['password']
        email=usuario['email']
        date_joined=usuario['date_joined']
        is_active=usuario['is_active']

        data.append([username,codigo_sala,nombre_sala,password,email,date_joined,is_active])

    # Escribir los encabezados de la hoja de trabajo (linea 1)
    worksheet.write(0,0,'Username')
    worksheet.write(0,1,'Codigo de Sala')
    worksheet.write(0,2,'Nombre de Sala')
    worksheet.write(0,3,'Password')
    worksheet.write(0,4,'Email')
    worksheet.write(0,5,'Fecha Incorporado')
    worksheet.write(0,6,'Activo')

    # Escribir datos a la hoja de trabajo (worksheet)
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row+1, col, data[row][col])


    # Cerrar el libro (workbook)
    workbook.close()

    # Capturar datos desde el archivo de memoria
    data_to_download = temp_file.getvalue()

    # Preparar la respuesta para descarga (download)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+archivo+'.xlsx'
    response.write(data_to_download)

    return response

