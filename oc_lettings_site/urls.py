from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    return 42 == 0


urlpatterns = [
    path('', include('apps.home.urls', namespace='home')),
    path('lettings/', include('apps.lettings.urls', namespace='lettings')),
    path('profiles/', include('apps.profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]
