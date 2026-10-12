from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

