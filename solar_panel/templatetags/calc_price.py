from django import template

register = template.Library()


@register.simple_tag
def calc_price(price, qty):
    all_price = price * qty
    return all_price
