from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion

#likes
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like





# Create your views here.

def base_usu(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/base_usu.html')

def inicio(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/inicio.html')

def publicaciones(request):
  publicaciones = Publicacion.objects.all()
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/publicaciones/publicaciones.html', {'publicaciones': publicaciones})

def convocatorias(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/convocatorias/convocatorias.html')

def productos(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/productos/productos.html')

def perfil(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/perfil.html')

def formulario_publicacion(request):
  if request.method == 'POST':
      form = formulario_publicacion(request.POST, request.FILES)
      if form.is_valid():
          form.save()

  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/publicaciones/formulario_publicacion.html', {'formulario_publicacion': formulario_publicacion})

def formulario_convocatoria(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/convocatorias/formulario_convocatoria.html')

def formulario_producto(request):
  return render(request, 'D:/Cultural__Code/Cultural_Expression/app_funcionalidad/templates/app_funcionalidad/productos/formulario_producto.html')



#likes

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    data = {
        'liked': liked,
        'count': post.likes.count()
    }
    return JsonResponse(data)
