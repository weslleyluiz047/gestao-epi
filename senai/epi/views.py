from django.shortcuts import render, redirect, get_object_or_404
from .forms import ColaboradorForm
from django.contrib import messages
from .models import Colaborador


def home(request):
    return render(request, 'epi/home.html')

def adicionar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return render(request, 'epi/adicionar_colaborador.html', {'form': form})  # Re-renderiza a página com a mensagem de sucesso
        else:
            messages.error(request, 'Erro ao cadastrar colaborador. Verifique os dados e tente novamente.')
            return render(request, 'epi/adicionar_colaborador.html', {'form': form})  # Re-renderiza a página com a mensagem de erro
    else:
        form = ColaboradorForm()

    return render(request, 'epi/adicionar_colaborador.html', {'form': form})

def relatorio_colaboradores(request):
    search_query = request.GET.get('search', '')
    if search_query:
        colaboradores = Colaborador.objects.filter(nome__icontains=search_query)
    else:
        colaboradores = Colaborador.objects.all()
    
    return render(request, 'epi/relatorio_colaboradores.html', {
        'colaboradores': colaboradores
    })

def colaborador_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        colaboradores = Colaborador.objects.filter(nome__icontains=search_query)
    else:
        colaboradores = Colaborador.objects.all()
    
    return render(request, 'colaborador_list.html', {'colaboradores': colaboradores})

def deletar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if request.method == 'POST':
        colaborador.delete()
        return redirect('nome_da_sua_lista_colaboradores')  # Trocar para o nome correto da URL

    return render(request, 'confirmar_delecao.html', {'colaborador': colaborador})

def equipamentos(request):
    return render(request, 'equipamentos.html')

