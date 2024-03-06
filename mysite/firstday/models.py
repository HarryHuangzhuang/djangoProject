from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length= 32)
    password = models.CharField(max_lenght = 64)
    age= models.IntegerField()



"""
他帮你翻译 自动操作
create table app01_userinfo(
    id vigint auto_increment primary key,
    name vachar(32),
    password varchar(64),
    age int
)


"""
