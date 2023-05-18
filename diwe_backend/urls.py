
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from diwe_backend import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('base.urls')),
    path('api/products/', include('diwe_product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
