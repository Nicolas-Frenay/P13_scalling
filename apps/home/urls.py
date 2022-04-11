from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('sentry-debug/', views.trigger_error, name='sentry_test'),
]
