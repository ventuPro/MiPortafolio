
from django.contrib import admin
from django.urls import path
from apps.cVentura.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.as_view(),name='index'),
]
