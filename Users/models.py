from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from simple_history.models import HistoricalRecords
    
class Commons(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('created_by'))
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
     

class User(AbstractUser,Commons):
    birthdate = models.DateField(null=True, blank=True, verbose_name=_('birthdate'))
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone'))
    address = models.TextField(null=True, blank=True, verbose_name=_('address'))
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('city'))
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True, verbose_name=_('image'))
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip'))
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
    )
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['username']
        default_permissions = ()
        permissions = [
            ('view_user', _('Can view user')),
            ('change_user', _('Can change user')),
            ('delete_user', _('Can delete user')),
            ('add_user', _('Can add user')),
        ]

    def __str__(self):
        return self.username
    
    def time_to_birthday(self):
        from datetime import date
        today = date.today()
        if self.birthdate:
            return self.birthdate - today
        return None


@receiver(post_migrate)
def create_initial_user(sender, **kwargs):
    if User.objects.count() == 0:
        User.objects.create_superuser(username='prueba', password='123456',first_name="Santiago", last_name="Britos")
    
    if Group.objects.count() == 0:
        Group.objects.create(name='Administrador')
        Group.objects.create(name='Almacenista')
        Group.objects.create(name='Supervisor')
        Group.objects.create(name='Operador')
        Group.objects.create(name='Vendedor')


