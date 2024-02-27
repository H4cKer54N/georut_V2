from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("login_title")
        return context
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', False)
        user = authenticate(self.request, **form.cleaned_data)
        if user is not None and user.is_active:
            login(self.request, user)
            if remember_me:
                self.request.session.set_expiry(30 * 24 * 60 * 60)
            else:
                self.request.session.set_expiry(24 * 60 * 60)
            return HttpResponseRedirect(self.get_success_url())
        else:
            # Añadir mensaje de error al formulario en caso de usuario inactivo o no autenticado correctamente
            form.add_error(None, _("Invalid username or password"))
            return self.form_invalid(form)
        
class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'update_user.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("update_user_title")
        
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save()
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    def get_object(self, queryset=None) -> User:
        return self.request.user