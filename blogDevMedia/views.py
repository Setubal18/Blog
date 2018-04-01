from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def postagem(request):
    postagem = Postagem.objects.all()
    postagens = {'lista': postagem}
    return render(request,'home.html', postagens)

def postagem_list(request, pk):
    post= get_object_or_404(Postagem,pk=pk)
    return render(request,'post.html', {'post':post})
