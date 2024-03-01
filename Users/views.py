import json
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from Users.forms import GroupPermissionForm, RememberMeAuthenticationForm
from .models import User, BaseGroup
from django.views.generic import UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import  Permission
from georut.settings import CREATED_APPS
from django.contrib import messages
from django.utils.decorators import method_decorator
from index.decorators import check_permissions_view

def logout_view(request):
    logout(request)
    return redirect('home')


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    form_class = RememberMeAuthenticationForm

    def get_context_data(self, **kwargs) -> dict[str, str]:
        context = super().get_context_data(**kwargs)
        context['title'] = _("Login")
        return context

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', False)
        user = authenticate(self.request, **form.cleaned_data)
        if user is not None and user.is_active:
            login(self.request, user)
            print(remember_me)
            print(form.cleaned_data)
            if remember_me:
                print("Remember me")
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
        context['title'] = _("Update user")

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

@method_decorator(check_permissions_view('view_group'), name='dispatch')
class ListGroupsPermissions(LoginRequiredMixin, ListView):
    template_name = 'groupsPermissions.html'
    model = BaseGroup

    def get_context_data(self, **kwargs) -> dict[str, str]:
        labels = Permission.objects.filter(content_type__app_label__in=CREATED_APPS)
        labeler_dict = []

        for label in labels:
            if "historical" not in label.name:
                labeler_dict.append(label)
                
        context = super().get_context_data(**kwargs)
        context['labeler'] = labeler_dict
        context['title'] = _("Groups and permissions")
        context['subtitle'] = _("This page deals with the management of user groups and permissions in the system.")
        return context
    
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')

        if action == "change_permissions" and request.user.groups.filter(permissions__codename="change_permissions_group").exists():
            try:
                group = request.POST.get('group')
                permissions = json.loads(request.POST.get('checkeds'))
                group = BaseGroup.objects.get(id=group)
                group.permissions.clear()
                for i in permissions:
                    permission = Permission.objects.get(id=i)
                    group.permissions.add(permission)
                message_info = {
                    'title': _('Perfect!'),
                    'text': _('Permissions updated successfully'),
                    'icon': 'success',  
                    }
                messages.success(request, message=message_info)
                return JsonResponse({},status=200,safe=True,)
            except Exception as e:
                print(e)
        if action == "delete" and request.user.groups.filter(permissions__codename="delete_group").exists():
            group = request.POST.get('group')
            group = BaseGroup.objects.get(id=group)
            group.delete()
            message_info = {
                'title': _('Perfect!'),
                'text': _('Group deleted successfully'),
                'icon': 'success',  
                }
            messages.success(request, message=message_info)
            return JsonResponse({},status=200,safe=True,)
        if action == "add" and request.user.groups.filter(permissions__codename="add_group").exists():
            
            group = request.POST.get('group')
            try:
                group = BaseGroup.objects.create(name=group)
            except Exception as e:
                print(e)
                if "UNIQUE" in str(e):
                    return JsonResponse({"message":_("A group with that name already exists.")},status=400,safe=True,)
                return JsonResponse({"message":_("Generic error, Contact administrator")},status=400,safe=True,)
            message_info = {
                'title': _('Perfect!'),
                'text': _('Group created successfully'),
                'icon': 'success',  
                }
            messages.success(request, message=message_info)
            return JsonResponse({},status=200,safe=True,)
        if action=="change" and request.user.groups.filter(permissions__codename="change_user").exists():
            group = request.POST.get('group')
            groupid = request.POST.get('groupid')
            try:
                groups = BaseGroup.objects.get(id=int(groupid))
                groups.name = group
                groups.save()
            except Exception as e:
                print(str(e))
                if "UNIQUE" in str(e):
                    return JsonResponse({"message":_("A group with that name already exists.")},status=400,safe=True,)
                return JsonResponse({"message":_("Generic error, Contact administrator")},status=400,safe=True,)
            message_info = {
                'title': _('Perfect!'),
                'text': _('Group created successfully'),
                'icon': 'success',  
                }
            messages.success(request, message=message_info)
            return JsonResponse({},status=200,safe=True,)
        else:
            return JsonResponse({"message":_("Generic error, Contact administrator")},status=400,safe=True,)
        
