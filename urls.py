from django.contrib import  admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('', views.PostList.as_view()),
    path('<int:pk>/', views.detailpost),
]