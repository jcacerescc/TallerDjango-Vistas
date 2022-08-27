from django.contrib import admin
from django.urls import path
from . import views
urlspatterns={
    path('', views.measurements_view, name='measurements_view'),
}