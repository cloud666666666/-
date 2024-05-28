from django.db import models

# Create your models here.



class test(models.Model):
    uname = models.CharField(max_length=32)
    upwd = models.CharField(max_length=64)