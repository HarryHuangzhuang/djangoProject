from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
from django.core.cache import cache as default_cache


class IpThrottle(SimpleRateThrottle):
    # 读取唯一标识                      访问记录 （redis）
    cache = default_cache

    scope = "ip"  # user
    # THROTTLE_RATES =  { "XXX": "5/m"}
    def get_cache_key(self, request, view):
        # 产生唯一标识  unique key
        if request.user:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        # throttle_u throttle_user_11.11.11.11 ser_2
        # cache_format = 'throttle_XXX_%(ident)s'  throttle_XXX_11.11.11.11 ident ip address
        return self.cache_format % {"scope": self.scope, "ident": ident}


class UserThrottle1(SimpleRateThrottle):
    # 读取唯一标识                      访问记录 （redis）
    cache = default_cache

    scope = "user"  # user
    # THROTTLE_RATES =  { "XXX": "5/m"}
    def get_cache_key(self, request, view):
        # 产生唯一标识  unique key
        if request.user:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        # throttle_u throttle_user_11.11.11.11 ser_2
        # cache_format = 'throttle_XXX_%(ident)s'  throttle_XXX_11.11.11.11 ident ip address
        return self.cache_format % {"scope": self.scope, "ident": ident}
