from django.contrib import admin
from .models import Category, Area

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_l', 'name')
    list_display_links = ('category_l',)
    list_editable = ('name',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('areacode_m', 'name')
    list_display_links = ('areacode_m',)
    list_editable = ('name',)
