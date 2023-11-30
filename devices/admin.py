from django.contrib import admin

from .models import Locals, Enviroments, Devices


@admin.register(Locals)
class LocalAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'color']


@admin.register(Enviroments)
class EviromentAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'color']


@admin.register(Devices)
class DeviceAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'color']