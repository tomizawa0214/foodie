from django.contrib import admin
from .models import Category, Pref

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_1', 'name')
    list_display_links = ('category_1',)
    list_editable = ('name',)

@admin.register(Pref)
class PrefAdmin(admin.ModelAdmin):
    list_display = ('pref', 'name')
    list_display_links = ('pref',)
    list_editable = ('name',)
