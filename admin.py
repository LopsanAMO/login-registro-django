from django.contrib import admin

from .models import Usuario

@admin.register(Usuario)

class AdminUsuario(admin.ModelAdmin):
    list_display = ('id','nombre','ap_paterno','foto','tipo')
    list_filter = ('tipo',)
