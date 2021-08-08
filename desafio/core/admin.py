from django.contrib import admin

from .models import State, City


class CityInLine(admin.TabularInline):
    model = City
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


class StateModelAdmin(admin.ModelAdmin):
    inlines = (CityInLine,)
    list_display = ('code', 'name')
    search_fields = list_display
    list_filter = list_display


class CityModelAdmin(admin.ModelAdmin):
    list_display = ('state', 'name', 'slug')
    search_fields = list_display
    list_filter = list_display
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(State, StateModelAdmin)
admin.site.register(City, CityModelAdmin)
