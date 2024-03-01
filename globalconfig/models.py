from django.db import models
from django.utils.translation import gettext as _
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

class GlobalConfig(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True, verbose_name=_('Company name to show on app'), default='Georut')
    logo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('Logo of company to show on app'))
    
    number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Id of company'))
    name_documents = models.CharField(max_length=100, verbose_name=_('Company name to show on documents'))
    logo_documents = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('Company logo to show on documents'))
    address = models.CharField(max_length=255,  null=True, blank=True, verbose_name=_('Company address to show on documents'))
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Company phone to show on documents'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('Company email to show on documents'))
    web = models.URLField(null=True, blank=True, verbose_name=_('Company web to show on documents'))
    historical = HistoricalRecords()

    class Meta:
        verbose_name = _('Global config')
        verbose_name_plural = _('Global Configs')
        default_permissions = ()
        permissions = [
            ('view_global_conf', _('Can view global conf')),
            ('change_global_conf', _('Can change global conf')),
            ('delete_global_conf', _('Can delete global conf')),
            ('add_global_conf', _('Can add global conf')),
        ]
    def __str__(self) -> str:
        return self.name
    
@receiver(post_migrate)
def create_initial_user(sender, **kwargs):
    if GlobalConfig.objects.count() == 0:
        GlobalConfig.objects.create(name='Georut', number='123456789', name_documents='Georut', address='Calle 123', phone='123456789',)