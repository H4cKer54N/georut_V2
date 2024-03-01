from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("Home")
        return context
    