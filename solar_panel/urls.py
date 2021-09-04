from django.urls import path
from solar_panel.views import *

urlpatterns = [
    path('', index, name='home'),
]
