from django.db import models

# Create your models here.
class UserInfo(models.Model):

    """user table"""
    choice  = (
        (1,"总监"),
        (2,"经理"),
        (3,"员工")
    )
    role = models.IntegerField(verbose_name = "role",choices = choice,default = 3)
    username = models.CharField(verbose_name = "username",max_length=32)
    password = models.CharField(verbose_name = "password",max_length=32)
    
    # 临时方式  jwt 
    token =  models.CharField(verbose_name = "TOKEN", max_length = 64,null=True,blank = True )