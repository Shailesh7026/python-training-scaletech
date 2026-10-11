from django.urls import path
from . import views;

urlpatterns = [
    path("",views.RoleView.as_view(),name="roles"),
    path("<int:role_id>",views.RoleView.as_view(),name="roles_detail"),
]
