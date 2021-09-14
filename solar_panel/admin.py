from django.contrib import admin
from .models import Photo, Product, Clients


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'power', 'area', 'region')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
    list_display_links = ('name', 'phone_number')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Clients, ClientAdmin)

admin.site.site_header = 'SolarEnergy'
