# Importa los módulos necesarios
import os
import sys

# Agrega la ruta a tu proyecto Django
sys.path.append('./')
os.environ['DJANGO_SETTINGS_MODULE'] = 'georut.settings'

# Inicializa Django
import django
django.setup()

groups = [
    "Inventarista",
    "Vendedor",
    "Transportista"
]

from Users.models import User, CustomGroup
from django.contrib.auth.models import Permission
user = User.objects.create_superuser(username="prueba", password="123456",first_name="Santiago",last_name="Britos")
admin,created = CustomGroup.objects.get_or_create(name="Administrador")
user.groups.add(admin)
for i in groups:
    CustomGroup.objects.get_or_create(name=i)
for i in Permission.objects.all():
    admin.permissions.add(i)
print("Usuarios insertados exitosamente.")
