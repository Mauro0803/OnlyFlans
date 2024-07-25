from django.contrib import admin
from django.urls import path, include
from web.views import index, about, welcome, contacto, exito, detalle_flan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('welcome/', welcome),
    path('about/', about),
    path('exito/', exito),
    path("contacto/", contacto),
    path("accounts/", include("django.contrib.auth.urls")),
    path('detalle_flan/<int:id>/', detalle_flan, name='detalle_flan'),
]
