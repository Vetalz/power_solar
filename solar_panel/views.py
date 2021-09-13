from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.filter(pk__lte=6)
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


def single_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Конкретный проект'
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