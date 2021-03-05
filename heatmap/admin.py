from django.contrib import admin
from .models import Point

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'lat', 'lon')