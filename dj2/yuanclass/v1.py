
    

# 创建class 的方法 type("类名"，（父类），{成员})

Foo1 = type("Foo",(object,),{"v1":123, "func":lambda self:999})




# class type:
#     def __init__(self):
#         pass  在空值
#     def __new__(self) :
#        先创建 new  pass  创建空值
  

  

class MyType(type):
    def __new__(cls,name,bases,attrs):

        del attrs["v1"]
        attrs["dex"] = "xxxx"
        xx = super().__new__(cls,name,bases,attrs)
        print("creat ",xx)
        return xx


class Base(object,metaclass = MyType):
    pass
 
class Foo(object,metaclass = MyType):
    pass