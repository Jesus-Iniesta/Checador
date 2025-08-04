from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    """
    Render the registration page.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Checks:login')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

@login_required(login_url='Checks:login')
def home(request):
    """
    Render the home page.
    """
    return render(request, 'Checador/check_tablero.html')