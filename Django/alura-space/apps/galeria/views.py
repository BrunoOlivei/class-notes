from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

def index(request):
    '''Função para renderizar a página inicial'''
    if not request.user.is_authenticated: # Se o usuário não estiver autenticado
        messages.error(request, "Usuário não autenticado!") # Mensagem de erro
        return redirect('login') # Redireciona para a página de login
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True) # Pega as fotografias do banco de dados
    return render(request, 'galeria/index.html', {"cards": fotografias}) # Renderiza a página inicial com as fotografias

def imagem(request, foto_id):
    '''Função para renderizar a página de imagem'''
    if not request.user.is_authenticated: # Se o usuário não estiver autenticado
        messages.error(request, "Usuário não autenticado!") # Mensagem de erro
        return redirect('login') # Redireciona para a página de login
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Pega a fotografia do banco de dados com base no id
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia}) # Renderiza a página de imagem com a fotografia

def buscar(request):
    '''Função para buscar fotografias'''
    if not request.user.is_authenticated: # Se o usuário não estiver autenticado
        messages.error(request, "Usuário não autenticado!") # Mensagem de erro
        return redirect('login') # Redireciona para a página de login
    
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True) # Pega as fotografias do banco de dados

    if "buscar" in request.GET: # Se o termo de busca estiver na requisição
        termo = request.GET["buscar"] # Pega o termo de busca
        if termo: # Se o termo de busca não estiver vazio
            fotografias = fotografias.filter(nome__icontains=termo) # Filtra as fotografias pelo nome
    return render(request, 'galeria/index.html', {"cards": fotografias}) # Renderiza a página inicial com as fotografias

def nova_imagem(request):
    '''Função para renderizar a página de nova imagem'''
    if not request.user.is_authenticated: # Se o usuário não estiver autenticado
        messages.error(request, "Usuário não autenticado!") # Mensagem de erro
        return redirect('login') # Redireciona para a página de login
    form = FotografiaForms() # Cria um formulário de fotografia

    if request.method == "POST": # Se o método da requisição for POST
        form = FotografiaForms(request.POST, request.FILES) # Cria um formulário de fotografia com os dados da requisição
        if form.is_valid(): # Se o formulário for válido
            form.save() # Salva o formulário
            messages.success(request, "Imagem cadastrada com sucesso!") # Mensagem de sucesso
            return redirect('index') # Redireciona para a página inicial

    return render(request, 'galeria/nova_imagem.html', {'form': form}) # Renderiza a página de nova imagem com o formulário

def editar_imagem(request, foto_id):
    '''Função para editar uma imagem'''
    fotografia = Fotografia.objects.get(pk=foto_id) # Pega a fotografia do banco de dados com base no id
    form = FotografiaForms(instance=fotografia) # Cria um formulário de fotografia com a fotografia

    if request.method == "POST": # Se o método da requisição for POST
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia) # Cria um formulário de fotografia com os dados da requisição e a fotografia
        if form.is_valid(): # Se o formulário for válido
            form.save() # Salva o formulário
            messages.success(request, "Imagem editada com sucesso!") # Mensagem de sucesso
            return redirect('index') # Redireciona para a página inicial

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id}) # Renderiza a página de editar imagem com o formulário e o id da fotografia

def deletar_imagem(request, foto_id):
    '''Função para deletar uma imagem'''
    fotografia = Fotografia.objects.get(pk=foto_id) # Pega a fotografia do banco de dados com base no id
    fotografia.delete() # Deleta a fotografia
    messages.success(request, "Imagem deletada com sucesso!") # Mensagem de sucesso
    return redirect('index') # Redireciona para a página inicial

def filtro(request, categoria):
    '''Função para filtrar fotografias por categoria'''
    if not request.user.is_authenticated: # Se o usuário não estiver autenticado
        messages.error(request, "Usuário não autenticado!") # Mensagem de erro
        return redirect('login') # Redireciona para a página de login
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True, categoria=categoria) # Pega as fotografias do banco de dados com base na categoria
    return render(request, 'galeria/index.html', {"cards": fotografias}) # Renderiza a página inicial com as fotografias
