from  rest_framework import  serializers
from rest_framework_jwt.settings import api_settings
from .models import Userinfo,Groupuser,ClientUser,SFunMsgs
import random
import re

'''
序列化一些model
'''




# 用户表的序列化
class CreateUserSerializer(serializers.ModelSerializer):
    user_account = serializers.CharField(label='账号',write_only=True,)
    password2 = serializers.CharField(label='确认密码', write_only=True)
    token = serializers.CharField(label='token',read_only=True)
    class Meta:
        model = Userinfo
        fields = ('id','user_account','password','password2','token')

# 注册用户时的序列化
class RegisterSerializer(serializers.ModelSerializer):
    user_account = serializers.CharField(label='账号')
    password2 = serializers.CharField(label='确认密码',write_only=True)
    password = serializers.CharField(label='密码')
    username = serializers.CharField(label='用户名称')
    info = serializers.CharField(label='用户信息')
    u_phone = serializers.CharField(label='用户电话')
    ip = serializers.CharField(label='最后一次登录的ip',read_only=True)
    updated = serializers.CharField(label='最后一次登录时间',read_only=True)
    is_status = serializers.CharField(label='用户启用状态')
    is_superadmin = serializers.CharField(label='是否是超级管理员')
    class Meta:
        model = Userinfo
        fields = ('id','user_account','password','password2','username','info','u_phone','ip','updated','is_status','is_superadmin')





# 分组信息序列化
class GroupuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupuser
        fields = "__all__"




# 客户模块的序列化
class ClientSerializer(serializers.ModelSerializer):
    group_id = serializers.CharField(label='分组id')
    client_name = serializers.CharField(label='用户昵称')
    group_name = serializers.CharField(label='用户组',read_only=True)
    class Meta:
        model = ClientUser
        fields = ('group_id','client_name','group_name')



class SFunSerializer(serializers.ModelSerializer):
    class Meta:
        model = SFunMsgs
        fields = "__all__"