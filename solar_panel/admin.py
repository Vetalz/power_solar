from django.contrib import admin
from .models import Photo, Product, Clients, Panel, Inverter, Category


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


class PanelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'sale')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'sale')


class InverterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'sale')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'sale')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Clients, ClientAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(Inverter, InverterAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'SolarEnergy'
