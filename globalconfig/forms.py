from django import forms
from .models import GlobalConfig
from django.utils.translation import gettext as _

class GlobalConfigForm(forms.ModelForm):
    class Meta:
        model = GlobalConfig
        fields = "__all__"
        labels = {
            "name":_("Company name to show on app"),
            "logo":_("Logo of company to show on app"),
            "number":_("Id of company"),
            "name_documents":_("Company name to show on documents"),
            "logo_documents":_("Company logo to show on documents"),
            "address":_("Company address to show on documents"),
            "phone":_("Company phone to show on documents"),
            "email":_("Company email to show on documents"),
            "web":_("Company web to show on documents"),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',"placeholder": _('Company name to show on app')}),
            'logo': forms.ClearableFileInput(attrs={'class': 'custom-file-input',"accept":"image/*"}),
            'number': forms.TextInput(attrs={'class': 'form-control',"placeholder": _('Id of company')}),
            'name_documents': forms.TextInput(attrs={'class': 'form-control',"placeholder": _('Company name to show on documents')}),
            'logo_documents': forms.ClearableFileInput(attrs={'class': 'form-control',"accept":"image/*"}),
            'address': forms.TextInput(attrs={'class': 'form-control',"placeholder": _('Company address to show on documents')}),
            'phone': forms.TextInput(attrs={'class': 'form-control',"placeholder": _('Company phone to show on documents')}),
            'email': forms.EmailInput(attrs={'class': 'form-control',"placeholder": _('Company email to show on documents')}),
            'web': forms.URLInput(attrs={'class': 'form-control',"placeholder": _('Company web to show on documents')}),            
        }
    

