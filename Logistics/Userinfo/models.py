from django.db import models
import django.utils.timezone as timezone
# Create your models here.



# 创建用户表
class Userinfo(models.Model):
    user_account= models.CharField(max_length=10,verbose_name='账号')
    username = models.CharField(max_length=10,verbose_name='用户名称')
    password = models.CharField(max_length=10,verbose_name='用户密码')
    token = models.CharField(max_length=255,verbose_name='token信息')
    info = models.CharField(max_length=100,verbose_name='描述')
    u_phone = models.CharField(max_length=30,verbose_name='用户手机')
    ip = models.CharField(max_length=50,verbose_name='ip')
    updated = models.DateTimeField(verbose_name='创建时间',default = timezone.now)
    creat_at = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    is_status = models.CharField(max_length=50,verbose_name='用户使用状态')
    is_superadmin = models.CharField(max_length=10,verbose_name='是否是超级管理员')
    class Meta:
        db_table ='user_userinfo'
        verbose_name = '账户信息表'
        verbose_name_plural = verbose_name
        unique_together = ('user_account','u_phone')





# 创建角色分类表
class Groupuser(models.Model):

    group_name = models.CharField(max_length=10, verbose_name='角色管理')
    updated = models.DateTimeField(verbose_name='创建时间',default = timezone.now)
    creat_at = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    class Meta:
        db_table ='user_groups'
        verbose_name ='用户组'
        verbose_name_plural = verbose_name
        unique_together = ('group_name', )
# 创建角色表
class ClientUser(models.Model):
    group = models.ForeignKey(Groupuser, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=10,verbose_name='用户名称')
    class Meta:
        db_table ='user_celinet'
        verbose_name ='客户模块角色表'
        verbose_name_plural = verbose_name
        unique_together = ('client_name', )




# 菜单栏表
class SFunMsgs(models.Model):
    menu_code = models.CharField(max_length=10,verbose_name='菜单栏的code')
    menu_name = models.CharField(max_length=30,verbose_name='菜单栏名称')
    url = models.CharField(max_length=30,verbose_name='url路径')
    menu_level = models.CharField(max_length=5,verbose_name='菜单栏的级别')
    father_code = models.CharField(max_length=10,verbose_name='父级菜单栏id')
    updated = models.DateTimeField(verbose_name='创建时间',default = timezone.now)
    creat_at = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    class Meta:
        db_table ='user_sfunmsgs'
        verbose_name = '导航栏表'
        verbose_name_plural = verbose_name
        unique_together = ('menu_code','menu_name','url','menu_level','father_code')