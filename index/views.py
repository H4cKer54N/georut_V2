from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

class Index(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("index_title")
        return context