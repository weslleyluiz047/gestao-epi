from django.urls import path, include
from .views import relatorio_colaboradores
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('adicionar_colaborador/', views.adicionar_colaborador, name='adicionar_colaborador'),
    path('relatorio_colaboradores/', views.relatorio_colaboradores, name='relatorio_colaboradores'),
    path('colaborador_list/', views.colaborador_list, name='colaborador_list'),
    path('colaboradores/', include('colaboradores.urls')),
]
