from django.urls import path
from .views import *
app_name="Users"

urlpatterns = [
    #GENERICS
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    
    #USERS
    path('update_user/', UpdateUser.as_view(), name='update_user'),
    path('groups/list', ListGroupsPermissions.as_view(), name='groups_list'),
]