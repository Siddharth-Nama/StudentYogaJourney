from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='sidd')
    email = models.EmailField(max_length=254,default='example@gmail.com')
    phone = models.CharField(max_length=15,default='+91987654321')
    dob = models.DateField(default='2004-04-26')
    image = models.ImageField(upload_to='profile')
    