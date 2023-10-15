from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    #created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image_preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',**NULLABLE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return (f'{self.name} {self.description} {self.category} '
                f'{self.purchase_price} {self.created_at} {self.updated_at}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='versions')
    number = models.CharField(max_length=100, verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.product} {self.number} {self.name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
