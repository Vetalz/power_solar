from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)

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
    main_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='product_photo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'СЭС'
        verbose_name_plural = 'СЭС'
