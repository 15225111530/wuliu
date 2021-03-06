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
    address = models.CharField(max_length=30,verbose_name='地址')
    phone = models.CharField(max_length=30,verbose_name='电话')
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


# 订单管理

class TheOrder(models.Model):
    order_number = models.CharField(max_length=100,verbose_name='订单号')
    data_times = models.CharField(max_length=100,verbose_name='订单时间')
    post_user = models.CharField(max_length=30,verbose_name='发货人')
    post_user_phone = models.CharField(max_length=30,verbose_name='发货人电话')
    post_user_address = models.CharField(max_length=30,verbose_name='发货人地址')
    get_user = models.CharField(max_length=30,verbose_name='收货人')
    get_user_phone = models.CharField(max_length=30,verbose_name='收货人电话')
    get_user_address= models.CharField(max_length=30,verbose_name='收货人地址')
    note = models.CharField(max_length=30,verbose_name='订单备注')
    status = models.CharField(max_length=30,verbose_name='订单状态')
    com_name = models.CharField(max_length=30,verbose_name='货物名称')
    com_number = models.CharField(max_length=30,verbose_name='货物数量')
    com_weight = models.CharField(max_length=30,verbose_name='货物重量')
    packaging = models.CharField(max_length=20,verbose_name='包装')
    single_price = models.CharField(max_length=30, verbose_name='单价')
    freight = models.CharField(max_length=30, verbose_name='运费')
    rebates = models.CharField(max_length=30, verbose_name='返款')
    transfer_fee = models.CharField(max_length=20,verbose_name='中转费')
    goods_note = models.CharField(max_length=30, verbose_name='货物备注')


    com_name1 = models.CharField(max_length=30,verbose_name='货物名称1')
    com_number1 = models.CharField(max_length=30,verbose_name='货物数量1')
    com_weight1 = models.CharField(max_length=30,verbose_name='货物重量1')
    packaging1 = models.CharField(max_length=20,verbose_name='包装')
    single_price1 = models.CharField(max_length=30, verbose_name='单价')
    freight1 = models.CharField(max_length=30, verbose_name='运费')
    rebates1 = models.CharField(max_length=30, verbose_name='返款')
    transfer_fee1 = models.CharField(max_length=20,verbose_name='中转费')
    goods_note1 = models.CharField(max_length=30, verbose_name='货物备注')

    com_name2 = models.CharField(max_length=30,verbose_name='货物名称2')
    com_number2 = models.CharField(max_length=30,verbose_name='货物数量2')
    com_weight2 = models.CharField(max_length=30,verbose_name='货物重量2')
    packaging2 = models.CharField(max_length=20,verbose_name='包装')
    single_price2 = models.CharField(max_length=30, verbose_name='单价')
    freight2 = models.CharField(max_length=30, verbose_name='运费')
    rebates2 = models.CharField(max_length=30, verbose_name='返款')
    transfer_fee2 = models.CharField(max_length=20,verbose_name='中转费')
    goods_note2 = models.CharField(max_length=30, verbose_name='货物备注')





    term_payment = models.CharField(max_length=30,verbose_name='付款方式')
    take_way = models.CharField(max_length=30,verbose_name='取件方式')


    all_freight =models.CharField(max_length=30,verbose_name='总运费')

    the_party1 = models.CharField(max_length=30,verbose_name='运输方1')
    the_party1_phone = models.CharField(max_length=30,verbose_name='运输方1电话')
    the_party1_address= models.CharField(max_length=30,verbose_name='运输方1地址')
    the_party2 = models.CharField(max_length=30,verbose_name='运输方2')
    the_party2_phone = models.CharField(max_length=30,verbose_name='运输方2电话')
    the_party2_address= models.CharField(max_length=30,verbose_name='运输方2地址')
    type = models.CharField(max_length=30,verbose_name='货物类型')

    class Meta:
        db_table ='the_order'
        verbose_name = '订单模块'
        verbose_name_plural = verbose_name
        unique_together = ('order_number','data_times',)

# 物流费用
class TLogCost(models.Model):
    provinces = models.CharField(max_length=30,verbose_name='省份')
    city = models.CharField(max_length=30,verbose_name='城市')
    county = models.CharField(max_length=30,verbose_name='县')
    tounsty = models.CharField(max_length=30,verbose_name='乡')
    money = models.CharField(max_length=30,verbose_name='费用')
    address = models.CharField(max_length=30,verbose_name='地址')


    class Meta:
        db_table ='tlog'
        verbose_name = '物流费用模块'
        verbose_name_plural = verbose_name
        unique_together = ('provinces','city','county','tounsty')