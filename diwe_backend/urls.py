
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('base.urls')),
    path('api/products/', include('diwe_product.urls')),
]
