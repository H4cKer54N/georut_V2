from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission, Group

class RememberMeAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=True, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label=_("Remember me")
    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.error_messages.update({
            'invalid_login': _("Please enter a correct username and password. Note that both fields may be case-sensitive."),
            'inactive': _("This account is inactive."),
        })


class GroupPermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['codename', 'name', 'content_type']

class GroupPermissionsForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Permisos'
    )

    class Meta:
        model = Group
        fields = ['name']