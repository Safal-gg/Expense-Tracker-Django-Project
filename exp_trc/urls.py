"""Defines url patterns for exp_trc (app)"""
from django.urls import path
from . import views

app_name='exp_trc'

urlpatterns=[

    path('',views.index,name='index'),
    path('new_expense/',views.create_expense,name='new'),
    path('read_expense/<int:expense_id>/',views.read_specific_expense,name='read_expense'),
    path('update_expense/<int:expense_id>/',views.update_specific_expense,name='update_expense'),
    path('delete_expense/<int:expense_id>/',views.delete_specific_expense,name='delete_expense'),

]
