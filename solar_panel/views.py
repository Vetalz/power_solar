import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Panel, Inverter, DELIVERY_CHOICES, REGION_CHOICES, PAYMENT_CHOICES
from .forms import ClientsForm, OrderForm
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


def equipment(request):
    anchor, form = req_form(request)
    categories = Category.objects.all()
    context = {
        'title': 'Оборудование',
        'anchor': anchor,
        'form': form,
        'categories': categories,

    }
    return render(request, 'solar_panel/equipment.html', context)


def single_panel(request, slug):
    anchor, form = req_form(request)
    item = get_object_or_404(Panel, slug=slug)
    context = {
        'equipment': item,
        'title': item.name,
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/single_equipment.html', context)


def single_inverter(request, slug):
    anchor, form = req_form(request)
    item = get_object_or_404(Inverter, slug=slug)
    context = {
        'equipment': item,
        'title': item.name,
        'anchor': anchor,
        'form': form
    }
    return render(request, 'solar_panel/single_equipment.html', context)


def cart(request):
    form = order_form(request)
    context = {
        'title': 'Ваш заказ',
        'form': form
    }
    return render(request, 'solar_panel/cart.html', context)


def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            messages.success(request, 'Заказ успешно оформлен. Наш менеджер свяжется с Вами')
            form = OrderForm()

            name = request.POST.get('name')
            phone = request.POST.get('phone')
            text = f'Имя: {name}\nТелефон: {phone}'
            delivery = request.POST.get('method_delivery')
            region = request.POST.get('region')
            payment = request.POST.get('method_payment')
            prod = json.loads(request.POST.get('product'))
            total_price = get_total_price(prod)
            instance.price = total_price

            for i in DELIVERY_CHOICES:
                if i[0] == delivery:
                    delivery = i[1]
            for i in REGION_CHOICES:
                if i[0] == region:
                    region = i[1]
            for i in PAYMENT_CHOICES:
                if i[0] == payment:
                    payment = i[1]

            context = {
                'title': 'SolarFuture.',
                'name': name,
                'phone': phone,
                'delivery': delivery,
                'region': region,
                'city': request.POST.get('city'),
                'new_post_office': request.POST.get('new_post_office'),
                'address': request.POST.get('address'),
                'comment': request.POST.get('comment'),
                'method_payment': payment,
                'product': prod,
                'total_price': total_price
            }

            email_html = render_to_string('solar_panel/email2.html', context)
            send_mail('💲Потенциальный клиент💲', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
                      html_message=email_html)
            instance.save()
        else:
            messages.error(request, 'Данные не отправлены')
    else:
        form = OrderForm()
    return form


def get_total_price(produce):
    total_price = 0
    for i in produce:
        price = i['price'] * i['qty']
        total_price += price
    return total_price
