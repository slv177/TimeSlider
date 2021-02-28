from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Person, Link, Link5

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'year')

@admin.register(Person)
class PersonAdmin(OSMGeoAdmin):
    list_display = ('name', 'surname')

@admin.register(Link)
class LinkAdmin(OSMGeoAdmin):
    list_display = ('name', 'year',)

@admin.register(Link5)
class LinkAdmin(OSMGeoAdmin):
    list_display = ('name',)