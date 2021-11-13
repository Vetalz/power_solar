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


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Panel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='panels', verbose_name='Категория')
    maker = models.CharField(max_length=150, verbose_name='Производитель')
    country = models.CharField(max_length=150, verbose_name='Страна производитель')
    type_panel = models.CharField(max_length=150, verbose_name='Тип панели', blank=True)
    material = models.CharField(max_length=150, verbose_name='Материал модуля', blank=True)
    power = models.PositiveIntegerField(verbose_name='Номинальная мощность, Вт', blank=True, null=True)
    voltage = models.FloatField(verbose_name='Напряжение при разомкнутом контуре, В', blank=True, null=True)
    short_circuit_current = models.FloatField(verbose_name='Ток короткого замыкания, А', blank=True, null=True)
    max_voltage = models.FloatField(verbose_name='Максимальное напряжение, В', blank=True, null=True)
    max_current = models.FloatField(verbose_name='Максимальный ток, А', blank=True, null=True)
    max_efficiency = models.FloatField(verbose_name='Максимальное КПД', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    short_description = models.TextField(verbose_name='Краткое описание')
    length = models.PositiveIntegerField(verbose_name='Длина, мм', blank=True, null=True)
    width = models.PositiveIntegerField(verbose_name='Ширина, мм', blank=True, null=True)
    thick = models.PositiveIntegerField(verbose_name='Толщина, мм', blank=True, null=True)
    weight = models.FloatField(verbose_name='Вес, кг', blank=True, null=True)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='panel_photo')
    price = models.DecimalField(verbose_name='Цена, грн', max_digits=5, decimal_places=0)
    sale = models.PositiveIntegerField(verbose_name='Скидка, %', null=True, blank=True)
    data_sheet = models.FileField(upload_to='equipment/panels', verbose_name='Спецификация', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Панель'
        verbose_name_plural = 'Панели'

    def get_absolute_url(self):
        return reverse('single_panel', kwargs={'slug': self.slug})


class Inverter(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='inverters', verbose_name='Категория')
    maker = models.CharField(max_length=150, verbose_name='Производитель')
    country = models.CharField(max_length=150, verbose_name='Страна производитель')
    power = models.PositiveIntegerField(verbose_name='Номинальная выходная мощность, кВт')
    max_power = models.PositiveIntegerField(verbose_name='Максимальная выходная мощность, кВт')
    mppt = models.PositiveIntegerField(verbose_name='Количество МРРТ', blank=True, null=True)
    dc_out = models.PositiveIntegerField(verbose_name='Количество DC выходов', blank=True, null=True)
    range_voltage = models.CharField(max_length=150, verbose_name='Диапазон напряжений для МРРТ', blank=True)
    max_efficiency = models.FloatField(verbose_name='Максимальное КПД', blank=True, null=True)
    min_temperature = models.IntegerField(verbose_name='Минимальная рабочая температура, град.', blank=True, null=True)
    max_temperature = models.IntegerField(verbose_name='Максимальная рабочая температура, град.', blank=True, null=True)
    protection = models.CharField(max_length=20, verbose_name='Степень защиты', blank=True)
    length = models.PositiveIntegerField(verbose_name='Длина, мм', blank=True, null=True)
    width = models.PositiveIntegerField(verbose_name='Ширина, мм', blank=True, null=True)
    thick = models.PositiveIntegerField(verbose_name='Толщина, мм', blank=True, null=True)
    weight = models.FloatField(verbose_name='Вес, кг', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    data_sheet = models.FileField(upload_to='equipment/panels', verbose_name='Спецификация', blank=True, null=True)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='inverter_photo')
    price = models.DecimalField(verbose_name='Цена, грн', max_digits=5, decimal_places=0)
    sale = models.PositiveIntegerField(verbose_name='Скидка, %', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инвертор'
        verbose_name_plural = 'Инверторы'

    def get_absolute_url(self):
        return reverse('single_inverter', kwargs={'slug': self.slug})


REGION_CHOICES = (
    ('02', 'Винницкая область'),
    ('03', 'Волынская область'),
    ('04', 'Днепропетровская область'),
    ('05', 'Донецкая область'),
    ('06', 'Житомирская область'),
    ('07', 'Закарпатская область'),
    ('08', 'Запорожская область'),
    ('09', 'Ивано-Франковская область'),
    ('10', 'Киевская область'),
    ('11', 'Киев'),
    ('12', 'Кировоградская область'),
    ('13', 'Луганская область'),
    ('14', 'Львовская область'),
    ('15', 'Николаевская область'),
    ('16', 'Одесская область'),
    ('17', 'Полтавская область'),
    ('18', 'Ровенская область'),
    ('19', 'Сумская область'),
    ('20', 'Тернопольская область'),
    ('21', 'Харьковская область'),
    ('22', 'Херсонская область'),
    ('23', 'Хмельницкая область'),
    ('24', 'Черкасская область'),
    ('26', 'Черновицкая область'),
    ('25', 'Черниговская область'),
)

DELIVERY_CHOICES = (
    ('1', 'Доставка по Украине'),
    ('2', 'Самовывоз в Кривом Роге')
)

PAYMENT_CHOICES = (
    ('1', 'Оплата наличными'),
    ('2', 'Наложенный платеж'),
    ('3', 'Оплата на расчетный счет ФОП')
)


ORDER_STATUS = (
    ('1', 'Новый'),
    ('2', 'В обработке'),
    ('3', 'Доставляется'),
    ('4', 'Успешный'),
    ('5', 'Неуспешный'),
)


class Order(models.Model):
    method_delivery = models.CharField(choices=DELIVERY_CHOICES, max_length=300, default=DELIVERY_CHOICES[0],
                                       verbose_name='Метод доставки')
    name = models.CharField(max_length=300, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    region = models.CharField(max_length=100, choices=REGION_CHOICES, blank=True, verbose_name='Область',
                              default=REGION_CHOICES[2])
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    new_post_office = models.CharField( max_length=300, verbose_name='Отделение Новой Почты', blank=True)
    address = models.CharField(max_length=300, blank=True, verbose_name='Адрес')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    method_payment = models.CharField(choices=PAYMENT_CHOICES, max_length=300, default=PAYMENT_CHOICES[0],
                                      verbose_name='Метод оплаты')
    product = models.JSONField(verbose_name='Товары')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default=ORDER_STATUS[0])
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.phone
