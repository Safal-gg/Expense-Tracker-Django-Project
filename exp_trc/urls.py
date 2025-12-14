"""Defines url patterns for exp_trc (app)"""
from django.urls import path
from . import views

app_name='exp_trc'

urlpatterns=[

    path('',views.index,name='index'),
    path('new_expense/',views.create_expense,name='new'),
]
