from rest_framework.permissions import BasePermission

import random

class MyPermission1(BasePermission):
    # code = 403 
    message = {"status" : False , "msg": "无权访问1"}
    def has_permission(self, request, view):

        # 获取请求中的数据，然后进行校验
        print("MyPermission1")
        return False
    

class MyPermission2(BasePermission):
    
    message = {"status" : False , "msg": "无权访问2"}
    def has_permission(self, request, view):

        # 获取请求中的数据，然后进行校验
        print("MyPermission2")
        return False
    
class MyPermission3(BasePermission):
    
    message = {"status" : False , "msg": "无权访问3"}
    def has_permission(self, request, view):

        # 获取请求中的数据，然后进行校验
        print("MyPermission3")
        return False