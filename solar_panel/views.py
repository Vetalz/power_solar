from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Product, Clients
from .forms import ClientsForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    anchor, form = req_form(request)
    products = Product.objects.all()[0:6]
    context = {
        'title': 'Главная',
        'products': products,
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/index.html', context)


def contact(request):
    anchor, form = req_form(request)
    context = {
        'title': 'Контакты',
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/contact.html', context)


def product(request):
    anchor, form = req_form(request)
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Наши проекты',
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/product.html', context)


def single_product(request, product_slug):
    anchor, form = req_form(request)
    current_product = get_object_or_404(Product, slug=product_slug)
    products = Product.objects.exclude(slug=product_slug)
    context = {
        'products': products,
        'current_product': current_product,
        'title': current_product.title,
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/single_product.html', context)


def ses_home(request):
    anchor, form = req_form(request)
    context = {
        'title': 'Электростанции для дома',
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/ses_home.html', context)


def ses_business(request):
    anchor, form = req_form(request)
    context = {
        'title': 'Электростанции для бизнеса',
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/ses_business.html', context)


def green_rate(request):
    anchor, form = req_form(request)
    context = {
        'title': 'Зелёный тариф',
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/green_rate.html', context)


def error404(request, exception):
    anchor, form = req_form(request)
    context = {
        'title': 'Страница не найдена',
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/404.html', context, status=404)


def req_form(request):
    anchor = None
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            anchor = request.POST.get('form_number')
            form.save()
            messages.success(request, 'Данные успешно отправлены')
            form = ClientsForm()
            name = request.POST.get('name')
            phone = request.POST.get('phone_number')

            text = f'Имя: {name}\nТелефон: {phone}'

            email_html = render_to_string('solar_panel/email.html',
                                          {'title': 'SolarFuture.', 'name': name, 'phone': phone})
            send_mail('💲Потенциальный клиент💲', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
                      html_message=email_html)
        else:
            messages.error(request, 'Данные не отправлены')
    else:
        form = ClientsForm()
    return anchor, form
