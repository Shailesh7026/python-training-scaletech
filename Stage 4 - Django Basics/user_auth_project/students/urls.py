
from django.urls import path
from .views import StudentView

urlpatterns = [
    path("", StudentView.as_view(), name="students"),
    path("<int:student_id>/", StudentView.as_view(), name="student_detail"),
]
