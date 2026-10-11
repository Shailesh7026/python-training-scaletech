from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserView.as_view(), name="users"),
    path("<int:user_id>/", views.UserView.as_view(),name="user_detail"),
]
