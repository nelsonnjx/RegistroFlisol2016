from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User



# Register your models here.
admin.site.register(Evento)
admin.site.register(Ponente)
admin.site.register(Asistente)
admin.site.register(Ponencia)
admin.site.register(Patrocinador)


class PonenteInline(admin.StackedInline):
    model = Ponente
    can_delete = False
    verbose_name_plural = 'Ponentes'

class UserAdmin(BaseUserAdmin):
    inlines = (PonenteInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)