from django.contrib import admin

from .models import TreeMenu


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'id',
        'name',
        'parent',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Enter menu name'
    prepopulated_fields = {
        'slug': ('name', )
    }