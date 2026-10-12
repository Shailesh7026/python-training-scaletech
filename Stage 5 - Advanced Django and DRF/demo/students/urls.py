from django.urls import path, include

# from .views import StudentListCreateAPIView, StudentDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r"students", StudentViewSet, basename="students")

urlpatterns = [
    # path('/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    # path('/<int:id>/', StudentDetailAPIView.as_view(), name='student-detail'),
    # routers urls
    path("", include(router.urls)),
]
