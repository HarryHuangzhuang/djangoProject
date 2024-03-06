from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def something(request):

    return HttpResponse("返回成功")


def login(request):
    return render(request,"login.html")