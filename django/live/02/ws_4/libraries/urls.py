from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('bestseller/', views.bestseller, name="bestseller"),
    path('recommend/', views.recommend, name="recommend"),
]
