from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=255 ,verbose_name="Название")

    description = models.TextField(
        null=True , blank=True ,verbose_name="Описание")

    price = models.DecimalField(
        default=0 ,
        max_digits=15,
        decimal_places = 2,
        verbose_name="Цена")

    sales = models.IntegerField(
        default=0,verbose_name="Кол-во продажи")

    avialable = models.BooleanField(
        default=True ,verbose_name="Есть в наличии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
    




