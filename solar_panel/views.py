from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.filter(pk__lte=6)
    context = {
        'title': 'Главная',
        'products': products,
    }
    return render(request, 'solar_panel/index.html', context)

