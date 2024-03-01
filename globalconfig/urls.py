
from django.urls import path
from .views import GlobalConfigView

urlpatterns = [
    path('globalconfig/', GlobalConfigView.as_view(), name='globalconfig'),
]
