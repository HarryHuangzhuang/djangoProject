from rest_framework.response import Response
import uuid
# Create your views here.
from rest_framework import request
from rest_framework.views import APIView
from api import models
from ext import code
from ext.perm import UserPermission, ManagerPermission,BossPermission
from ext.view import NbAPIView

from ext.throttle import IpThrottle,UserThrottle1

class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes= [IpThrottle,]
    # api_settings.DEFAULT_AUTHENTICATION_CLASSES
    # def get(self ,request):
    #     return Response("return success") 
    def perform_authentication(self, request):
        request.user

    def post(self, request):
        # 1.接受用户提交的用户名和密码
        # 2.数据库校验
        user = request.data.get("username")
        pwd = request.data.get("password")
        # print(request.queryset_params)  get url 中的 参数
        user_object = models.UserInfo.objects.filter(username = user,password = pwd).first()
        if not user_object:
            # return Response({"code":code.ERROR_CODE,"msg":"username or password error"})
            return Response({"status":False,"msg":"username or password error"})
        # if the user and password correct ,should create a token 
        token = str(uuid.uuid4())
        user_object.token = token
        user_object.save()
        return Response({"status":True,  "data":token}) 





class UserView(NbAPIView):
    # authentication_classes = []
    # 总监 或  员工 或 manager
    permission_classes = [UserPermission,ManagerPermission,BossPermission]
    def get(self ,request):
        print(request.user,request.auth) 
        return Response("return success  ")
    
    def post(self ,request):
        return Response()
    def put(self ,request):
        return Response()
    def delete(self ,request):
        return Response()


class OrderView(NbAPIView):
     # 总监 或  员工 或 manager
    permission_classes = [ManagerPermission,BossPermission]
    throttle_classes = [UserThrottle1,IpThrottle]
    def get(self ,request):
        print(request.user, request.auth)
        self.dispatch
        return Response({"status":True, "data": [11,22,33,44]}) 

class RoleOrderView(NbAPIView):
    # 总监 或  员工 
    permission_classes = [ManagerPermission,BossPermission]
    throttle_classes = [UserThrottle1]
    def get(self ,request):
        print(request.user, request.auth)
        self.dispatch
        return Response({"status":True, "data": [11,22,33,44]}) 
   
 
class InfoView(APIView):
    def get(self ,request):
        return Response("return success") 
    
