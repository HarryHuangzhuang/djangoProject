# from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response



class HomeView(APIView):
    # version_param = api_settings.VERSION_PARAM  因为这句话 所以配置文件里叫啥 传参 叫啥 这里叫version

    # http://127.0.0.1:8000/home/?xx=123&age=999&version=v1   ->request.version = v1 
    # versioning_class = URLPathVersioning 

    def get(self, request, *arg, **kwargs):
        print(request.version)
        print(request.versioning_scheme)  #为了反向生产url
        # url = request.versioning_scheme.reverse("hh", request=request)
       
        # print("反向生产的URL:",url)
        # self.dispatch
        return Response("...") 