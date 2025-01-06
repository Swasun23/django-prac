from django.contrib import admin
from .models import Role, Shift, Holiday

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'access_level')
    search_fields = ('name',)

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name','start_time', 'end_time')

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')
    search_fields = ('name', 'description')
    list_filter = ('date',)
