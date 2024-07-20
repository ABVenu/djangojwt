from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    USER_ROLES = (
        ('reader','Reader'),
        ('author','Author')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_ROLES)
    
    def __str__(self):
        return f'{self.user}-{self.user_type}'



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publihsed = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}-{self.author}'
