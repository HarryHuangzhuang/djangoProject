from django.db import models

# Create your models here.
class UserInfo(models.Model):



    username = models.CharField(verbose_name = "username",max_length=32)
    password = models.CharField(verbose_name = "password",max_length=32)
    
    # 临时方式  jwt 
    token =  models.CharField(verbose_name = "TOKEN", max_length = 64,null=True,blank = True )