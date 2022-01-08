from .models import Category, Income, Report, Expense
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput, Select


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ["title", "category", "comment", "sum", 'date']
        category = Category.objects.all()
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "category": Select(choices=category, attrs={'class': 'form-control', 'placeholder': 'Введите категорию'}),
            "comment": Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Введите комментарий'}),
            "sum": NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите сумму'}),
            "date": DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату'}), }


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["title", "category", "comment", "sum", 'date']
        category = Category.objects.all()
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "category": Select(choices=category, attrs={'class': 'form-control', 'placeholder': 'Введите категорию'}),
            "comment": Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Введите комментарий'}),
            "sum": NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите сумму'}),
            "date": DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату'}), }


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ["xfrom", "to"]
        widgets = {
            "xfrom": DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату'}),
            "to": DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату'})}
