from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^asistentes/$', views.asistentes, name='asistentes'),
    url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^userprofile/$', views.userprofile, name='userprofile'),
    url(r'^asistente/(?P<id>\d+)$', views.asisdata, name='asistente'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home.html'}, name='logout'),
    url(r'^$', views.home, name='home'),
]
