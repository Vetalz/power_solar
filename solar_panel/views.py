from django.shortcuts import render, get_object_or_404
from .models import Product, Photo


def index(request):
    products = Product.objects.all()[0:6]
    context = {
        'title': 'Главная',
        'products': products,
    }
    return render(request, 'solar_panel/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'solar_panel/contact.html', context)


def product(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Наши проекты',
    }
    return render(request, 'solar_panel/product.html', context)


def single_product(request, product_slug):
    current_product = get_object_or_404(Product, slug=product_slug)
    products = Product.objects.exclude(slug=product_slug)
    context = {
        'products': products,
        'current_product': current_product,
        'title': current_product.title,
    }
    return render(request, 'solar_panel/single_product.html', context)


def ses_home(request):
    context = {
        'title': 'Электростанции для дома'
    }
    return render(request, 'solar_panel/ses_home.html', context)


def ses_business(request):
    context = {
        'title': 'Электростанции для бизнеса'
    }
    return render(request, 'solar_panel/ses_business.html', context)


def green_rate(request):
    context = {
        'title': 'Зелёный тариф'
    }
    return render(request, 'solar_panel/green_rate.html', context)
