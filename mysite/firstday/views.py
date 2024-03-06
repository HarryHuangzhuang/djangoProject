from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login.html")  
        #获取POST 提交的数据
    username = request.POST.get("user")
    password= request.POST.get("pwd")
    if username == "root" and password =="123":
        return HttpResponse("登录成功")
    return render(request, "login.html", {"error_msg":"用户名或密码错误"})