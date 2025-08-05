from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from Checks.models import WorkSession
from django.utils import timezone

def register(request):
    """
    Render the registration page.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}! Ahora puedes iniciar sesión.')
            # Opcional: Iniciar sesión automáticamente después del registro
            # login(request, user)
            # return redirect('Checks:home')
            return redirect('Checks:login')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

@login_required(login_url='Checks:login')
def home(request):
    """
    Render the home page.
    """
    #Buscar si hay una sesión abierta (sin registro de salida)
    session = WorkSession.objects.filter(user=request.user, end_time__isnull=True).first()

    if request.method == "POST":
        if session:
            #registrar salida
            session.end_time = timezone.now()
            session.save()
        else:
            #Registrar entrada
            WorkSession.objects.create(user=request.user, start_time=timezone.now())
        return redirect('Checks:home')
    #Historiall de sesiones
    sessions = WorkSession.objects.filter(user=request.user).order_by('-start_time')

    return render(request, 'Checador/check_tablero.html',{
        'session': session,
        'sessions': sessions
    })