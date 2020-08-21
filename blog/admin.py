from django.contrib import admin
from .models import Categoria,Posteo
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PosteoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Posteo,PosteoAdmin)
