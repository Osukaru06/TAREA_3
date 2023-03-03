from django.shortcuts import render
from .models import Post,Categoria
from django.db.models import Q
from django.core.paginator import Paginator
#Crear vistas

def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset)
            ).distinct()
        
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)    
    
    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    return render(request,'post.html',{'detalle_post':post})

def critica(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Critica')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Critica'),
        ).distinct()

    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'critica.html',{'posts':posts})

def estrenos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Estrenos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Estrenos'),
        ).distinct()

    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'estrenos.html',{'posts':posts})

def animacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Animacion')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Animacion'),
        ).distinct()

    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'animacion.html',{'posts':posts})

def internacional(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Internacional')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Internacional'),
        ).distinct()

    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'internacional.html',{'posts':posts})

def clasico(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Cine Clasico')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Cine Clasico'),
        ).distinct()
    
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'clasico.html',{'posts':posts})