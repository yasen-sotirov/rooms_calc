# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_list, name='text_list'),
    path('new/', views.text_new, name='text_new'),
    path('<int:pk>/edit/', views.text_edit, name='text_edit'),
]
