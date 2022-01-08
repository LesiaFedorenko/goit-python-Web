from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from django.db.models import Sum


def index(request):
    incomes = Income.objects.order_by('-id')[:5]
    expenses = Expense.objects.order_by('-id')[:5]
    balance1 = Income.objects.all().aggregate(sum=Sum('sum')).get('sum')
    if balance1 == None:
        balance1 = 0
    balance2 = Expense.objects.all().aggregate(sum=Sum('sum')).get('sum')
    if balance2 == None:
        balance2 = 0
    balance = balance1 - balance2
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'incomes': incomes, "expenses": expenses, "balance1": balance1,
                   "balance2": balance2, "balance": balance})


def about(request):
    return render(request, 'main/about.html')


def create_expense(request):
    error = ''
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"
    form = ExpenseForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_expense.html', context)


def create_income(request):
    error = ''
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"
    form = ExpenseForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_income.html', context)


def search(request):
    error = False
    if 'q1' and 'q2' in request.GET:
        q1 = request.GET['q1']
        q2 = request.GET['q2']
        if not q1:
            error = True
        elif not q2:
            error = True
        else:
            incomes = Income.objects.filter(date__range=[q1, q2])
            expenses = Expense.objects.filter(date__range=[q1, q2])
            balance1 = Income.objects.all().filter(date__range=[q1, q2]).aggregate(sum=Sum('sum')).get('sum')
            if balance1 == None:
                balance1 = 0
            balance2 = Expense.objects.all().filter(date__range=[q1, q2]).aggregate(sum=Sum('sum')).get('sum')
            if balance2 == None:
                balance2 = 0
            balance = balance1 - balance2
            return render(request, 'main/report.html',
                          {'incomes': incomes, "expenses": expenses, "balance1": balance1, "balance2": balance2,
                           "balance": balance, "xfrom": q1, 'to': q2})
    return render(request, 'main/search_form.html', {'error': error})


