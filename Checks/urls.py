from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'Checks'
urlpatterns = [
    path('', views.home, name='home'),  # URL raíz que va al home
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('home/', views.home, name='home'),  # Mantener esta por compatibilidad
    path('logout/', LogoutView.as_view(next_page='Checks:login'), name='logout'),
]