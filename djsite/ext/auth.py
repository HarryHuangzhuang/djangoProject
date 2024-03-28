from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models


class QueryParamsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 去做用户认证
        # 1.读取请求传递的token
        # 2.校验token 的合法性
        # 3.返回值
        # 3。1 返回元组 （11，22）认证成 request.user ,request.auth
        # 3.2 抛出异常  认证失败 ——》返回错误信息
        # 3.3 返回None  多个认证类[类1，类2，类3]  -》 匿名用户
        token = request.query_params.get("token")  # 从url 中 拿token
        if not token:
            return
        user_object = models.UserInfo.objects.filter(
            token=token
        ).first()  # chick in the database

        if user_object:
            return user_object, token  # request.user = 用户对象 request.auth = token
        # raise AuthenticationFailed("failed")
        # raise AuthenticationFailed({"code":2000,"error":"authentication failed"})
        return

    def authenticate_header(self, request):
        return "API"


class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):

        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            return
        user_object = models.UserInfo.objects.filter(token=token).first()

        if user_object:
            return user_object, token  # request.user = 用户对象 request.auth = token
        # raise AuthenticationFailed("failed")
        return

    def authenticate_header(self, request):
        return "API"


class NoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        raise AuthenticationFailed({"status": False, "msg": "认证失败"})

    def authenticate_header(self, request):
        return "API"
