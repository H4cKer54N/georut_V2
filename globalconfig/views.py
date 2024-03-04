from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from index.decorators import check_permissions_view
from .models import GlobalConfig
from .forms import GlobalConfigForm
from django.contrib import messages
@method_decorator(check_permissions_view('view_global_conf'), name='dispatch')
class GlobalConfigView(LoginRequiredMixin, UpdateView):
    template_name = 'globalConfig.html'
    model = GlobalConfig
    form_class = GlobalConfigForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return GlobalConfig.objects.first()

    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("Global Configuration")
        context['subtitle'] = _("In order to ensure a seamless and personalized user experience, our application offers a comprehensive set of global configurations. These settings allow you to customize key elements that reflect your brand identity and business information.")
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if self.request.user.groups.filter(permissions__codename="change_global_conf").exists():
            message_info = {
                    'title': _('Perfect!'),
                    'text': _('Global config updated successfully'),
                    'icon': 'success',  
                    }
            messages.success(self.request, message=message_info)
            return super().form_valid(form)
        
        return render(self.request, '403.html', status=403)
        
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        message_info = {
                'title': _('Error!'),
                'text': _('Please check the form and try again'),
                'icon': 'error',  
                }
        messages.error(self.request, message=message_info)
        return super().form_invalid(form)
    



def custom_404(request, exception):
    return render(request, '404.html', status=404, context={'title': 'Error 404'})

def custom_403(request, exception):
    return render(request, '403.html', status=403, context={'title': 'Error 403'})
