from django.shortcuts import redirect, render
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


from firstday.models import Department,UserInfo


def orm(request):
    # Department.objects.create(title = "销售部")
    # Department.objects.create(title = "IT部")
    # Department.objects.create(title = "运营部") 
    # 增加 
    # UserInfo.objects.create(name = "zhuanghuang",password = "123", age = 19)
    # UserInfo.objects.create(name = "zhangsan",password = "123", age = 19)
    # UserInfo.objects.create(name = "lisi",password = "123", age = 19)
     
    UserInfo.objects.all().delete()



    #获取数据ite

    # queryset = UserInfo.objects.all()
    # for obj in queryset:
    #     print(obj.id,obj.name,obj.password,obj.age)
    return HttpResponse("成功")


def info_list(request):
    data_list = UserInfo.objects.all()
    # print(data_list)



    return render(request,"info_list.html", {"data_list": data_list})

def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")


    UserInfo.objects.create(name =user,password = pwd ,age=age)
    # return redirect("http://127.0.0.1:8000/info/list/")
    return redirect("/info/list/")


