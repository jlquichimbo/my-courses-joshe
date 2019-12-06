from django.urls import path, include
from app import views

urlpatterns = [
    # Index landing page
    path('', views.index_page, name='index'),
    path('inicio/', views.inicio, name = 'inicio'),
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.cerrar_sesion, name = 'logout'),
]
