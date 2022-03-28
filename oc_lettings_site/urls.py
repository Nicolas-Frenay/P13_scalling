from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('apps.lettings.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('admin/', admin.site.urls),
]
