from django.db import models
from django.urls import reverse


class Photo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True, related_name='photos')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    power = models.FloatField(verbose_name='Мощность, кВт')
    area = models.FloatField(verbose_name='Площадь, м2')
    region = models.CharField(max_length=100, verbose_name='Область')
    generation = models.FloatField(verbose_name='Генерация в год, кВт')
    profit = models.FloatField(verbose_name='Прибыль в год, $')
    is_green_rate = models.BooleanField(verbose_name='Зелёный тариф', default=False)
    main_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='product_photo')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('single_product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'СЭС'
        verbose_name_plural = 'СЭС'


class Clients(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
