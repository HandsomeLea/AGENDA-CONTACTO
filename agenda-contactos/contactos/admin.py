from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contacto

#superusuario o Admin para el Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'correo')
