from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('user/',views.UserView.as_view(),name="user")
]