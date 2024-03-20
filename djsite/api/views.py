from rest_framework.response import Response
import uuid
# Create your views here.
from rest_framework import request

from rest_framework.views import APIView



from api import models
from ext import code
class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
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





class UserView(APIView):


    def get(self ,request):
        print(request.user,request.auth) 
        return Response("return success  ")
    
    def post(self ,request):
        return Response()
    def put(self ,request):
        return Response()
    def delete(self ,request):
        return Response()

from ext.perm import MyPermission1,MyPermission2,MyPermission3
class OrderView(APIView):

    permission_classes = [MyPermission1,MyPermission2,MyPermission3]
    def get(self ,request):
        print(request.user, request.auth)
        self.dispatch
        return Response({"status":True, "data": [11,22,33,44]}) 
    

    def check_permissions(self, request):
        Permission_objects = self.get_permissions()
        no_permission_objects = []
        
        for permission in Permission_objects:
            if permission.has_permission(request,self):
                return 
            else:
                no_permission_objects.append(permission)
             
        else:
            self.permission_denied(
                request,
                message=getattr(no_permission_objects[0],"message",None),
                code= getattr(no_permission_objects[0],"code",None)
            )
 
class InfoView(APIView):
    def get(self ,request):
        return Response("return success") 