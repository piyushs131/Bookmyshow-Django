from django.contrib import admin
from .models import Seat

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('movie', 'row', 'number', 'is_booked')
    list_filter  = ('movie', 'is_booked')
    search_fields = ('movie__title', 'row', 'number')
