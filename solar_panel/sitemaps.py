from django.contrib.sitemaps import Sitemap
from .models import Product
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return ['home', 'contact', 'product', 'ses_home', 'ses_business', 'green_rate']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Product.objects.all()
