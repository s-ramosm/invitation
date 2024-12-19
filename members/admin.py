from django.contrib import admin
from .models import Event, Item, Guest, GuestItem

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')
    search_fields = ('name',)
    ordering = ['start_time']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'image')
    search_fields = ('name', 'event__name')

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password')  # Campos que se mostrarán en la lista
    search_fields = ('name',)  # Permite buscar por nombre
    list_filter = ('name',)  # Filtra por nombre


@admin.register(GuestItem)
class GuestItemAdmin(admin.ModelAdmin):
    list_display = ('guest', 'item', 'confirmed')  # Mostrar invitado, item y estado de confirmación
    list_filter = ('guest', 'item', 'confirmed')  # Filtros para facilitar la búsqueda
    search_fields = ('guest__name', 'item__name') 

