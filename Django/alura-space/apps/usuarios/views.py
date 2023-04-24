from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms

def login(request):
    '''Função para fazer login'''
    form = LoginForms() # Instancia o formulário

    if request.method == "POST": # Se o método for POST
        form = LoginForms(request.POST) # Pega os dados do formulário

        if form.is_valid():
            nome = form["nome_login"].value() # Pega o valor do campo nome
            senha = form["senha"].value() # Pega o valor do campo senha
        
        usuario = auth.authenticate( # Autentica o usuário com base no
            request, 
            username=nome,  # Nome do usuário
            password=senha # Senha do usuário
        )

        if usuario is not None: # Se o usuário existir
            auth.login(request, usuario) # Faz o login
            messages.success(request, f'{nome} logado com sucesso!') # Mensagem de sucesso
            return redirect('index') # Redireciona para a página inicial
        else: # Se o usuário não existir
            messages.error(request, 'Usuário ou senha inválidos!') # Mensagem de erro
            return redirect('login') # Redireciona para a página de login

    return render(request, 'usuarios/login.html', {'form': form}) # Renderiza a página de login

def cadastro(request):
    '''Função para fazer cadastro'''
    form = CadastroForms() # Instancia o formulário

    if request.method == "POST": # Se o método for POST
        form = CadastroForms(request.POST) # Pega os dados do formulário

        if form.is_valid(): # Se o formulário for válido
            nome = form["nome_cadastro"].value() # Pega o valor do campo nome
            email = form["email"].value() # Pega o valor do campo email
            senha = form["senha_1"].value() # Pega o valor do campo senha 1

            if User.objects.filter(username=nome).exists(): # Se o usuário já existir
                messages.error(request, "Usuário já existe!") # Mensagem de erro
                return redirect('cadastro') # Redireciona para a página de cadastro
            
            usuario = User.objects.create_user(username=nome, email=email, password=senha) # Cria o usuário
            usuario.save() # Salva o usuário no banco de dados
            messages.success(request, f'{nome} cadastrado com sucesso!') # Mensagem de sucesso
            return redirect('login') # Redireciona para a página de login

    return render(request, 'usuarios/cadastro.html', {'form': form}) # Renderiza a página de cadastro

def logout(request): # Função para fazer logout
    auth.logout(request) # Faz o logout
    messages.success(request, 'Logout com sucesso!') # Mensagem de sucesso
    return redirect('login') # Redireciona para a página de login