from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # Название товара
    description = models.TextField()  # Описание товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    image = models.ImageField(upload_to='products/')  # Изображение товара
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.name
