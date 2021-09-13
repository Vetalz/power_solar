from django.contrib import admin
from .models import Photo, Product


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'power', 'area', 'region')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'SolarEnergy'
