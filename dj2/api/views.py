# from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser,FileUploadParser
from rest_framework.negotiation import DefaultContentNegotiation

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