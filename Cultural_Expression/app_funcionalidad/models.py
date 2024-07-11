from django.db import models

from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')



class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'categoria'


    def __str__(self):
        fila_categoria = "ID:" + self.id_categoria + "--" + "Nombre Categoria:" + self.nombre_categoria
        return fila_categoria


class Convocatoria(models.Model):
    id_convocatoria = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    lugar = models.CharField(max_length=50)
    foto = models.ImageField( upload_to='D:/Cultural__Code/Cultural_Expression/app_funcionalidad/static/app_funcionalidad/img/img_convocatorias/', blank=True, null=True)
    fecha_convocatoria = models.DateField()

    class Meta:
        managed = False
        db_table = 'convocatoria'

    def __str__(self):
        fila_convocatoria = "ID:" + self.id_convocatoria + "--" + "ID_Usuario:" + self.id_usuario + "ID_Categoria:" + self.id_categoria + "--" + "Titulo:" + self.titulo + "--" + "Descripcion:" + self.descripcion + "--" + "Fecha Inicio:" + self.fecha_inicio + "--" + "Fecha Fin:" + self.fecha_fin + "--" + "Lugar:" + self.lugar + "--" + "Fecha:" + self.fecha_convocatoria
        return fila_convocatoria
    
    def delete(self, using=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=400)
    precio = models.IntegerField()
    archivo_multimedia = models.ImageField( upload_to='D:/Cultural__Code/Cultural_Expression/app_funcionalidad/static/app_funcionalidad/img/img_productos/', blank=True, null=True)
    fecha_producto = models.DateField()

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        fila_producto = "ID:" + self.id_producto + "--" + "ID_Usuario:" + self.id_usuario + "--" + "ID_Categoria:" + self.id_categoria + "--" + "Nombre:" + self.nombre_producto + "--" + "Descripcion:" + self.descripcion + "--" + "Precio:" + self.precio + "--" + "Fecha:" + self.fecha_producto
        return fila_producto
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo_multimedia.storage.delete(self.archivo_multimedia.name)
        super().delete()



class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    foto = models.ImageField( upload_to='D:/Cultural__Code/Cultural_Expression/app_funcionalidad/static/app_funcionalidad/img/img_publicaciones/', blank=True, null=True)
    fecha_publicacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'publicacion'

    def __str__(self):
        fila_publicacion = "ID:" + self.id_publicacion + "--" + "ID_Usuario:" + self.id_usuario + "--" + "ID_Categoria:" + self.id_categoria + "--" + "Titulo:" + self.titulo + "--" + "Descripcion:" + self.descripcion + "Fecha:" + self.fecha_publicacion
        return fila_publicacion
    
    def delete(self, using=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()



class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10, blank=True, null=True)
    gmail = models.CharField(unique=True, max_length=40)
    alias = models.CharField(unique=True, max_length=25)
    contrasenia = models.CharField(max_length=20)
    foto_perfil = models.ImageField(upload_to='D:/Cultural__Code/Cultural_Expression/app_funcionalidad/static/app_funcionalidad/img/img_perfil/', blank=True, null=True)
    rol = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


    def __str__(self):
        fila_usuario = "ID:" + self.id_usuario + "--" + "Alias:" + self.alias + "--" + "Contacto:" + self.gmail
        return fila_usuario
    
    def delete(self, using=None, Keep_parents=False):
        self.foto_perfil.storage.delete(self.foto_perfil.name)
        super().delete()