from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^asistente$', views.asistente, name='asistente'),
    url(r'^login$', views.login, name='login'),
    url(r'^$', views.home, name='home'),
]
