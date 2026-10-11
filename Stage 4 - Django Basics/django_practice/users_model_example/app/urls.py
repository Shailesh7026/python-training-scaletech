from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_user , name="list_user"),
    path('edit/<int:user_id>',views.edit_user, name="edit_user"),
    path('add/', views.add_user , name="add_user"),
]
