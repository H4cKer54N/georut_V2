from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group as BaseGroup
from simple_history.models import HistoricalRecords
    
class Commons(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Created by'))
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
     

class User(AbstractUser,Commons):
    birthdate = models.DateField(null=True, blank=True, verbose_name=_('Birthdate'))
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('Phone'))
    address = models.TextField(null=True, blank=True, verbose_name=_('Address'))
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('City'))
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True, verbose_name=_('Image'))
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('Ip'))
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        verbose_name=_('Groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        verbose_name=_('User permissions'),
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


class CustomGroup(BaseGroup):
    history = HistoricalRecords(inherit=True)
    
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        default_permissions = ()
        permissions = [
            ('view_group', _('Can view group')),
            ('change_group', _('Can change group')),
            ('delete_group', _('Can delete group')),
            ('add_group', _('Can add group')),
            ('change_permissions_group', _('Can change permissions group')),
            ('view_permissions_group', _('Can view permissions group')),
        ]
