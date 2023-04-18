from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_adicao").filter(publicada=True)

    if "buscar" in request.GET:
        termo = request.GET["buscar"]
        if termo:
            fotografias = fotografias.filter(nome__icontains=termo)
    return render(request, 'galeria/buscar.html', {"cards": fotografias})
