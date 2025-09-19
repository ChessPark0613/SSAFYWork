from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_todo, name='create'),
    path('<path:work>/', views.detail, name='detail'),
]
