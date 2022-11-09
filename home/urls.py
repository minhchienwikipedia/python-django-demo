from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.item_search_views),
    path('create/', views.item_create_views),
]
