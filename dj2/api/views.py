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
class D1(serializers.ModelSerializer):
    class Meta:
        model = models.Depart
        fields  =  ["id","title"]

class D2(serializers.ModelSerializer):
    ex = serializers.SerializerMethodField()
    class Meta:
        model = models.Tag
        # fields  =  "__all__"
        fields  =  ["caption","ex"]

    def get_ex(self,obj):
        return "xxx"
#1.在类成员中删除
#2.汇总到  BaseSerializer._declared_fields    {yy:对象}
class BaseSerializer(serializers.Serializer):
    yy = serializers.CharField(source = 'name')
    name = 123


#1.在类成员中删除
#2.汇总到  BaseSerializer._declared_fields    {xx:对象，yy:对象}
class UserSerializer(serializers.ModelSerializer,BaseSerializer):
    #  source 后面直接接方法名称
    #  gender = serializers.CharField(source = "get_gender_display")
    # gender_text = serializers.CharField(source = "get_gender_display")
    # depart = serializers.CharField(source = "depart.title")
    # ctime = serializers.DateTimeField(format="%Y-%m-%d")
  
    depart = D1()
    tags = D2(many = True)
     
    # xxx = serializers.SerializerMethodField()    
    class  Meta:
        model =models.UserInfo
        # fields = "__all__"

        fields = ["name","age","depart","tags"]

    # def get_xxx(self,obj):

    #     # result = []
    #     queryset = obj.tags.all()  #因为是多对多 那么 
    #     # for tag in queryset:
    #     #     result.append({"id":tag.id,"caption":tag.caption})
    #     result = [{"id":tag.id,"caption":tag.caption} for tag in queryset ]
        
    #     return result




# 运行django 项目，创建字段对象
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
from  django.core.validators import RegexValidator
from  rest_framework import exceptions
class DepartmentSerializer(serializers.Serializer):
    # username = serializers.CharField(required=True)
    # password = serializers.CharField(required=True)
    title = serializers.CharField(required=True, max_length=20, min_length=6)
    order = serializers.IntegerField(required=False, max_value=100, min_value=10)
    level = serializers.ChoiceField(choices=[("1", "高级"), (2, "中级")])

    # email = serializers.EmailField()
    # email = serializers.CharField(validators=[EmailValidator(message="邮箱格式错误")])

    email = serializers.CharField(validators=[RegexValidator(r"\d+", message="格式错误")])
    def validate_email(self, value):
        print(value)
        if len(value) > 6:
            raise exceptions.ValidationError("hooks vaild error")
        return value
    
    def validate(self, attrs):
        print("validate=", attrs)
        # api_settings.NON_FIELD_ERRORS_KEY
        # raise exceptions.ValidationError("全局钩子校验失败")
        return attrs
    # code = serializers.CharField()
class DepartmentView(APIView):
    def post(self,request,*args,**kwargs):
        # 1. get 原始data
        print(request.data)
        # 2.校验 （form +modelform） 后续还要 序列化  
        ser = DepartmentSerializer(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data)
        else:
            return Response(ser.errors)
        
        # return Response("...")
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