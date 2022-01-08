from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create_expense', views.create_expense, name='create_expense'),
    path('create_income', views.create_income, name='create_income'),
    path('search_form', views.search, name='search_form'),
]