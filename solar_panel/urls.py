from django.urls import path
from solar_panel.views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('ses-home/', ses_home, name='ses_home'),
    path('ses-business/', ses_business, name='ses_business'),
    path('product/<slug:product_slug>/', single_product, name='single_product'),
    path('green-rate/', green_rate, name='green_rate'),
    path('equipment/', equipment, name='equipment'),
    path('equipment/panels/<slug:slug>/', single_panel, name='single_panel'),
    path('equipment/inverters/<slug:slug>/', single_inverter, name='single_inverter'),
    path('cart/', cart, name='cart')
]
