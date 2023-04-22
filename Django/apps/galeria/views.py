from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não autenticado!")
        return redirect('login')
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não autenticado!")
        return redirect('login')
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não autenticado!")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True)

    if "buscar" in request.GET:
        termo = request.GET["buscar"]
        if termo:
            fotografias = fotografias.filter(nome__icontains=termo)
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    return render(request, 'galeria/nova_imagem.html')

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass
