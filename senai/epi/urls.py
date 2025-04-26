# epi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('adicionar-colaborador/', views.adicionar_colaborador, name='adicionar_colaborador'),
    path('relatorio_colaboradores/', views.relatorio_colaboradores, name='relatorio_colaboradores'),
    path('editar_colaborador/<int:colaborador_id>/', views.editar_colaborador, name='editar_colaborador'),
    path('deletar_colaborador/<int:colaborador_id>/', views.deletar_colaborador, name='deletar_colaborador'),
]
