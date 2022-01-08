from django.contrib import admin
from .models import Category, Income, Report, Expense

admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Report)
admin.site.register(Expense)

