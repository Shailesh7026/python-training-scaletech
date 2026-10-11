from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     db_table = "users"
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"
        
    #     constraints=[
    #         models.CheckConstraint(
    #             condition=Q(marks.__gte=0),
    #             name="Age Should be positive"
    #         )
    #     ]