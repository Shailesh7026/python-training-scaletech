from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',include("authentication.urls")),
    path('api/v1/users/',include("users.urls")),
    path('api/v1/roles/',include("roles.urls")),
     path("api/v1/students/", include("students.urls")),
]
