from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from index.decorators import check_permissions_view

@method_decorator(check_permissions_view('view_global_conf'), name='dispatch')
class GlobalConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'globalConfig.html'

    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("Global Configuration")
        return context
    
def custom_404(request, exception):
    return render(request, '404.html', status=404, context={'title': 'Error 404'})
