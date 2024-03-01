from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('set_language/', set_language, name='set_language'),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # path('articles/', include('Articles.urls')),
    # path('categories/', include('Categories.urls')),
    # path('clients/', include('Clients.urls')),
    # path('iva/', include('Iva.urls')),
    # path('orders/', include('Orders.urls')),
    path('', include('Users.urls')),
    # path('vehicles/', include('Vehicles.urls')),
    # path('warehouse/', include('Warehouse.urls')),
    path('', include('index.urls')),
    path('', include('globalconfig.urls')),

)

handler404 = 'globalconfig.views.custom_404'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)