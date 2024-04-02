# from django.shortcuts import render

# # Create your views here.
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser,FileUploadParser
from rest_framework.negotiation import DefaultContentNegotiation
from api import models 
from rest_framework import serializers

class DepartSerializer(serializers.ModelSerializer):
    class  Meta:
        model =models.Depart
        fields = "__all__"



class DepartView(APIView):
    def get(self,request,*args,**akwrgs):
        #1.获取数据库的数据{id:xxx,title ..}
       
       queryset = models.Depart.objects.all()
        #2.转换成json 格式 : int/str/list
       
       ser = DepartSerializer(instance= queryset,many = True)

       print(ser.data) #{title ：“技术不”，count：10}
        #3.返回个用户
       context = {"status":True , "data":ser.data}
       return Response(context)

class UserSerializer(serializers.ModelSerializer):
    #  source 后面直接接方法名称
    #  gender = serializers.CharField(source = "get_gender_display")
    gender_text = serializers.CharField(source = "get_gender_display")
    ctime = serializers.DateTimeField(format="%Y-%m-%d")
     
    xxx = serializers.SerializerMethodField()
    class  Meta:
        model =models.UserInfo
        # fields = "__all__"

        fields = ["name","age","gender","gender_text","ctime","xxx"]

    def get_xxx(self,obj):
        
        return "{}-{}-{}".format(obj.name,obj.age,obj.gender)

class UserView(APIView):
    def get(self,request,*args,**akwrgs):
        
        # models.UserInfo.objects.all().update(ctime = datetime.datetime.now()) 
        #1.获取数据库的数据
        queryset =  models.UserInfo.objects.all()

      
        #2.转换成json 格式 : int/str/list
        ser = UserSerializer(instance= queryset,many = True)

      

     
        #3.返回个用户
        context = {"status":True , "data":ser.data}
        return Response(context)








class HomeView(APIView):
    # version_param = api_settings.VERSION_PARAM  因为这句话 所以配置文件里叫啥 传参 叫啥 这里叫version

    # http://127.0.0.1:8000/home/?xx=123&age=999&version=v1   ->request.version = v1 
    # versioning_class = URLPathVersioning 
    parser_classes = [JSONParser, FormParser,FileUploadParser]
    # JSONParser    data_dict =    json.load()

    # FormParser  ,解析器  x=123&age=11   QueryDict request.POST

    
    # 根据请求去匹配对应的解析器  ；寻找渲染器
    content_negotiation_class = DefaultContentNegotiation

    def get(self, request, *arg, **kwargs):
        print(request.version)
        print(request.versioning_scheme)  #为了反向生产url
        # url = request.versioning_scheme.reverse("hh", request=request)
       
        # print("反向生产的URL:",url)
        # self.dispatch
        return Response("...") 
    
    def post(self, request,*arg,**kwargs):
        print(request.data)
        print(request.data,type(request.data))
        self.dispatch

        #         return Request(
        #     request,
        #     parsers=self.get_parsers(),      
        #     authenticators=self.get_authenticators(),
        #     negotiator=self.get_content_negotiator(),
        #     parser_context=parser_context
        # )   封装到request 里了           data_dict =json.load()
        return Response("请求来了 ")