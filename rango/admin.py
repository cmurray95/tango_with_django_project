from django.contrib import admin
from rango.models import Category, Page


# Page admin panel config
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


# Categories admin panel config
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
