from django.db import models
from django.contrib.auth.models import User

class AuthProfile(models.Model):
    """One user can have one author profile -- One to One RelationShip"""
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Profile of {self.user.name}"
    
class Tag(models.Model):
    """Multiple Blogs can have multiple Tags -- Many to Many RelationShip"""
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    """One author can have multiple blogs -- One to Many RelationShip"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag,related_name="blogs",blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title

    # Custom Model Method
    def word_count(self):
        """Count Words"""
        return len(self.content.split())