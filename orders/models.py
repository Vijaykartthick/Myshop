from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class address(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address_line = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=80)
    pincode = models.CharField(max_length=10)
    is_default = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_created=True)

