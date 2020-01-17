from rest_framework.permissions import BasePermission
from .models import Userinfo
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from django.http import JsonResponse

'''
自定义一些方法
'''



class MyPermission(BasePermission):
    def has_permission(self, request, view):
        """判断对使用此权限类的视图是否有访问权限"""
        # 任何用户对使用此权限类的视图都没有访问权限
        token = request.META.get('HTTP_AUTHORIZATION', None)
        token_obj = Userinfo.objects.filter(token=token).first()

        if not token_obj:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        """判断对使用此权限类视图某个数据对象是否有访问权限"""
        # 需求: 对id为1，3的数据对象有访问权限
        print(obj,'456')
        if obj.id in (5, 3):
            return True
        return False


# 自定义认证类

# 1）继承BaseAuthentication类
# 2）重新authenticate(self, request)方法，自定义认证规则
# 3）认证规则基于的条件：
#       没有认证信息返回None(游客)
#       有认证信息认证失败抛异常(非法用户)
#       有认证信息认证成功返回用户与认证信息元组(合法用户)
# 4）完全视图类的全局(settings文件中)或局部(确切的视图类)配置
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class MyAuthentication(BaseAuthentication):
    """
    同前台请求头拿认证信息auth（获取认证的字段要与前台约定）
    没有auth是游客，返回None
    有auth进行校验
        失败是非法用户，抛出异常
        成功是合法用户，返回 (用户, 认证信息)
    """
    def authenticate(self, request):
        # 前台在请求头携带认证信息，
        #       且默认规范用 Authorization 字段携带认证信息，
        #       后台固定在请求对象的META字段中 HTTP_AUTHORIZATION 获取
        auth = request.META.get('HTTP_AUTHORIZATION', None)

        # 处理游客
        if auth is None:
            raise AuthenticationFailed('未携带token，请携带token访问')
            # return None

        user = Userinfo.objects.filter(token=auth).first()
        if not user:
            raise AuthenticationFailed('token失效，请重新登录')
        return (user, None)
