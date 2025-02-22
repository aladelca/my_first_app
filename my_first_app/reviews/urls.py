from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_review, name='add_review'),
    path('list/', views.list_review, name='list_review'),
    ]