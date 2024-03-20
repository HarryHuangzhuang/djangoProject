from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length= 32)
    password = models.CharField(max_length = 64)
    
    # size = models.IntegerField()
    age= models.IntegerField(default = 2)
    # data = models.IntegerField(null = True, blank = True)
    account_salary = models.DecimalField(verbose_name="账户余额", max_digits = 10,decimal_places= 2 , default = 0)
    # 数据精确 decimal_places 总共10 位 小数位 为 2   
    create_time = models.DateTimeField(verbose_name= "入职时间" )
# 练级删除 
    # depart = models.ForeignKey(to="Department",to_field= "id",on_delete= models.CASCADE)
#    设置空
    depart = models.ForeignKey(to="Department",to_field= "id",null = True,blank = True,on_delete= models.SET_NULL)
    # django 
    gender_choices = (
        (1,"男"),
        (2,"女"),
    )

    gender = models.SmallIntegerField(verbose_name = "性别 ",choices = gender_choices,default = 1)


"""
他帮你翻译 自动操作
create table app01_userinfo(
    id vigint auto_increment primary key,
    name vachar(32),
    password varchar(64),
    age int
)
"""
class Department(models.Model):
    title = models.CharField(max_length=16)
# Department.objects.create(title = " 销售部")

class Role(models.Model):
    caption = models.CharField(max_length = 16)

# UserInfo.objects.create(name = "harry",password = 123145)
    # UserInfo.objects.delete().all()