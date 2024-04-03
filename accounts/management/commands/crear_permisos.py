from accounts.models import Usuario
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# para crear un permiso
# desde el directorio del proyecto y desde la linea de comando ejecutar:
# python manage.py crear_permisos
# es mejor hacerlo usando el atributo Meta permissions del modelo


content_type = ContentType.objects.get_for_model(Usuario)
permission = Permission.objects.create(
    codename='ver_menu_guias',
    name='Puede Ver Menu Guias',
    content_type=content_type,
)