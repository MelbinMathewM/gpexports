from django.db import models

# Create your models here.
class quote(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    message=models.CharField(max_length=100)