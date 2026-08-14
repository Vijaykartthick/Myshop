from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilePic(models.Model):
    profile = models.ImageField(upload_to='profile/',default='vijay.jpeg',)
    user = models.ForeignKey(User,on_delete=models.CASCADE)