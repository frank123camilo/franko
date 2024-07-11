from django.contrib import admin
from django.urls import path
from app_pag_static.views import base_pag_static, vista_principal, acerca_nosotros, reglas_negocio, terminos_condiciones
from app_funcionalidad.views import base_usu, inicio, publicaciones, convocatorias, productos, perfil, formulario_publicacion, formulario_convocatoria, formulario_producto
from app_registro_olvido.views import login


from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('base_pag_static/',base_pag_static),
    path('',vista_principal, name= "vista_principal"),
    path('acerca_nosotros/',acerca_nosotros, name= "acerca_nosotros"),
    path('reglas_negocio/',reglas_negocio, name= "reglas_negocio"),
    path('terminos_condiciones/',terminos_condiciones, name= "terminos_condiciones"),


    path('base_usu/',base_usu),
    path('inicio/',inicio, name= "inicio"),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('convocatorias/',convocatorias, name= "convocatorias"),
    path('productos/',productos, name= "productos"),
    path('perfil/',perfil, name="perfil"),
    path('formulario_publicacion/',formulario_publicacion, name= "formulario_publicacion"),
    path('formulario_convocatoria/',formulario_convocatoria, name= "formulario_convocatoria"),
    path('formulario_producto/',formulario_producto, name= "formulario_producto"),
    
    
    path('login/',login, name= "login")



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



