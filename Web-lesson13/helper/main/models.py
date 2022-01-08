from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')

    def __str__(self):
        return self.name


class Income(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField("Название", max_length=50)
    comment = models.TextField("Комментарий")
    sum = models.DecimalField('Сумма', max_digits=19, decimal_places=2)
    date = models.DateField('date published', default=date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    class Meta:
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField("Название", max_length=50)
    comment = models.TextField("Комментарий")
    sum = models.DecimalField('Сумма', max_digits=19, decimal_places=2)
    date = models.DateField('date published', default=date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"


class Report(models.Model):
    xfrom = models.DateField('date published', default=date.today)
    to = models.DateField('date published', default=date.today)
