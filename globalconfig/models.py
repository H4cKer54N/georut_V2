from django.db import models
from django.utils.translation import gettext as _
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

class GlobalConfig(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True, verbose_name=_('name_of_company'), default='Georut')
    logo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('logo_of_company'))
    
    number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('number_of_company'))
    name_documents = models.CharField(max_length=100, verbose_name=_('name_of_documents'))
    logo_documents = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('logo_of_documents'))
    address = models.CharField(max_length=255,  null=True, blank=True, verbose_name=_('address_of_company'))
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('phone_of_company'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email_of_company'))
    web = models.URLField(null=True, blank=True, verbose_name=_('web_of_company'))
    historical = HistoricalRecords()

    
    def __str__(self) -> str:
        return self.name
    
@receiver(post_migrate)
def create_initial_user(sender, **kwargs):
    if GlobalConfig.objects.count() == 0:
        GlobalConfig.objects.create(name='Georut', number='123456789', name_documents='Georut', address='Calle 123', phone='123456789',)