from django.db import models
from django.db import models
from django.conf import settings


class Student(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="student_profile"
    )

    roll_number = models.CharField(
        max_length=30,
        unique=True
    )

    age = models.PositiveIntegerField()

    course = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.roll_number}"

