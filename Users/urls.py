from django.urls import path
from .views import *

app_name="Users"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('update_user/', UpdateUser.as_view(), name='update_user'),
]