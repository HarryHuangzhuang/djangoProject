from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    # code = 403 
    message = {"status" : False , "msg": "无权访问1"}
    def has_permission(self, request, view):

        # 获取请求中的数据，然后进行校验
        if request.user.role == 3:
            return True
        return False
    

class ManagerPermission(BasePermission):
    
    message = {"status" : False , "msg": "无权访问2"}
    def has_permission(self, request, view):

        # 获取请求中的数据，然后进行校验
        if request.user.role == 2:
            return True
        return False
    
class BossPermission(BasePermission):
    
    message = {"status" : False , "msg": "无权访问3"}
    def has_permission(self, request, view):

        # 获取请求中的数据，然后进行校验
        if request.user.role == 1:
            return True
        return False