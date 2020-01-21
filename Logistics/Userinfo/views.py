
#导入第三方的模块
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import mixins,generics
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework import filters
import pandas as pd
# 导入自定义封装的方法
from .utils import MyPermission,MyAuthentication
from tools.get_ip import client_ip
from .serializers import CreateUserSerializer,RegisterSerializer,GroupuserSerializer,ClientSerializer,SFunSerializer,OrderSerializer,TLogCostSerializer,UpdaorderSerializer
from tools.newpage import PageViewSet
from .search import RegionFilter,tlogfilter,Search_user
# 导入model
from .models import  Userinfo,Groupuser,ClientUser,SFunMsgs,TheOrder,TLogCost
# Create your views here.



# 用户登录
class Login(viewsets.ModelViewSet,mixins.CreateModelMixin):
    # authentication_classes = [MyAuthentication]
    queryset = Userinfo.objects.all()
    serializer_class = CreateUserSerializer
    # permission_classes = [MyPermission]

    # 重写queryset方法，当获取到的token为空时，返回空，获取到token之后，之返回个人信息
    def get_queryset(self):
        auth = self.request.META.get('HTTP_AUTHORIZATION', None)
        if auth:
            user_obj = Userinfo.objects.filter(token=auth).first()
            return user_obj
        else:
            return None
    # 登录函数
    def create(self, request, *args, **kwargs):
        user_account = request.POST.get('user_account')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        uesr_query = Userinfo.objects.filter(user_account = user_account).first()
        ip = client_ip(request)
        if password ==password2:
            if uesr_query:
                if uesr_query.is_status == '1':
                    if password == uesr_query.password:
                        payload = jwt_payload_handler(uesr_query)
                        token = jwt_encode_handler(payload)
                        uesr_query.token = token
                        uesr_query.ip = ip
                        uesr_query.save()
                        return Response({"code":200,"token":token,'username':uesr_query.username,'is_superadmin':uesr_query.is_superadmin})
                    return  Response({"code":400,"msgs":'账户密码不对，请检查输入信息'})
                else:
                    return  Response({"code":400,"msgs":'账户已被禁用，请联系管理员进行启用'})
            return Response({"code":400,"msgs":'账号不存在，请注册'})
        return Response({"code": 400, "msgs": '两次输入密码不一致'})
# 用户注册页面
class Register(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    # authentication_classes = [MyAuthentication]
    queryset = Userinfo.objects.all()
    serializer_class = RegisterSerializer
    pagination_class = PageViewSet

    # permission_classes = [MyPermission]
    # 重写list方法，显示首页的人员信息
    def list(self, request):
        msgs = []
        instance_status  =Userinfo.objects.all()
        for y in instance_status:
            detail_dict = {}
            detail_dict['id']  = y.id
            detail_dict['user_account']  = y.user_account
            detail_dict['username']  = y.username
            detail_dict['info']  = y.info
            detail_dict['u_phone']  = y.u_phone
            detail_dict['ip']  = y.ip
            detail_dict['updated']  = y.updated
            detail_dict['is_status']  = y.is_status
            detail_dict['is_superadmin']  = y.is_superadmin
            msgs.append(detail_dict)
        return Response({"code": 200, "msgs": msgs})


    def retrieve(self, request, *args, **kwargs):
        id  = kwargs['pk']
        user = Userinfo.objects.filter(id=id).first()
        return Response({'id':id,'user_account':user.user_account,'password':user.password,'password2':user.password,'info':user.info,'is_status':user.is_status,'u_phone':user.u_phone,'username':user.username,'is_superadmin':user.is_superadmin})
    # 重写creat方法，用于注册人员时候使用
    def create(self, request, *args, **kwargs):
        try:
            user_account = request.POST.get('user_account')
            password2 = request.POST.get('password2')
            password =request.POST.get('password')
            username = request.POST.get('username')
            info = request.POST.get('info')
            u_phone =int(request.POST.get('u_phone'))
            is_superadmin = request.POST.get('is_superadmin')
            ip = client_ip(request)
            is_status = request.POST.get('is_status')
            if password2 == password:
                uesr_query = Userinfo.objects.filter(user_account =user_account).first()
                if uesr_query:
                    return Response({"code": 400, "msgs": '用户已经存在，直接登录'})
                Userinfo.objects.create(user_account=user_account, password=password, username=username, info=info,u_phone=u_phone, ip=ip,is_status = is_status,is_superadmin=is_superadmin)
                return Response({"code": 200, "msgs": '添加成功'})
            return Response({"code": 400, "msgs": '两次输入密码不一致'})
        except:
            return Response({"code": 400, "msgs": '请输入正确数据'})

    # 重写update方法,用于用户的修改
    def update(self, request, *args, **kwargs):
        u_id = kwargs['pk']
        password2 = request.POST.get('password2')
        password = request.POST.get('password')
        username = request.POST.get('username')
        is_superadmin = request.POST.get('is_superadmin')
        info = request.POST.get('info')
        u_phone = int(request.POST.get('u_phone'))
        ip = client_ip(request)
        is_status = request.POST.get('is_status')
        uesr_query = Userinfo.objects.filter(id=u_id).first()
        uesr_query.password = password
        uesr_query.password2 = password2
        uesr_query.username = username
        uesr_query.info = info
        uesr_query.u_phone = u_phone
        uesr_query.ip = ip
        uesr_query.is_status = is_status
        uesr_query.is_superadmin = is_superadmin
        uesr_query.save()

        # uesr_query.update(**{'password':password,'password2':password2,'username':username,'info':info,'u_phone':u_phone,'ip':ip,'group_id':group,'is_status':is_status})
        return Response({"code": 200, "msgs": '修改成功'})

    # 重写delete方法，用于用户的删除
    def destroy(self, request, *args, **kwargs):
        u_id =kwargs['pk']
        uesr_query = Userinfo.objects.filter(id=u_id).first()
        uesr_query.delete()
        return Response({"code": 200, "msgs": '修改成功'})
# 成员分组增删改查
class Group(viewsets.ModelViewSet):
    '''
    成员组信息的接口
    1、get请求
       返回结果： 所有的数据，有成员组id，成员组的名称
    2.post请求
       创建成员组信息，只需穿入group_name即可创建
    3.put请求
       传入id，进行成员组名字修改
    4.delete请求
       传入id，进行删除
    '''
    queryset = Groupuser.objects.all()
    serializer_class = GroupuserSerializer

# 添加客户管理模块
class Customer(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    # authentication_classes = [MyAuthentication]
    queryset = Userinfo.objects.all()
    serializer_class = ClientSerializer
    pagination_class = PageViewSet


    def list(self, request, *args, **kwargs):
        group_list = Groupuser.objects.all()
        msgs = []
        for x in group_list:
            instance_status  =ClientUser.objects.filter(group_id=x.id)
            if instance_status:
                for y in instance_status:
                    detail_dict = {}
                    detail_dict['id']  = y.id
                    detail_dict['group_name']  = x.group_name
                    detail_dict['client_name']  = y.client_name
                    detail_dict['address']  = y.address
                    detail_dict['phone']  = y.phone
                    msgs.append(detail_dict)
        return Response({"code": 200, "msgs": msgs})
    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        user = ClientUser.objects.filter(id=id).first()
        group_name = user.group.group_name
        group_id = user.group.id
        return Response({'id': id, 'client_name': user.client_name, 'group_id': group_id,'group_name':group_name,'address':user.address,'phone':user.phone})

    def create(self, request, *args, **kwargs):
        client_name = request.POST.get('client_name')
        group_id = request.POST.get('group_id')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        ClientUser.objects.create(client_name=client_name,group_id=group_id,address=address,phone=phone)
        return Response({"code": 200, "msgs": '添加成功'})
    def update(self, request, *args, **kwargs):
        id = kwargs['pk']
        client_name = request.POST.get('client_name')
        group_id = request.POST.get('group_id')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = ClientUser.objects.filter(id=id).first()
        user.client_name = client_name
        user.group_id = group_id
        user.address = address
        user.phone = phone
        user.save()
        return Response({"code": 200, "msgs": '修改成功'})

    def destroy(self, request, *args, **kwargs):
        u_id = kwargs['pk']
        uesr_query = ClientUser.objects.filter(id=u_id).first()
        uesr_query.delete()
        return Response({"code": 200, "msgs": '删除成'})
class SFunMsg(viewsets.ModelViewSet,mixins.UpdateModelMixin,ListAPIView):
    queryset = SFunMsgs.objects.all()
    serializer_class = SFunSerializer

    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        token_obj = Userinfo.objects.filter(token=token).first()
        if token_obj.is_superadmin == "1":
            msgs = []
            one_menu = SFunMsgs.objects.filter(menu_level =1)
            for menu in one_menu:
                dict = {}
                dict['menu_name'] = menu.menu_name
                two_menu = SFunMsgs.objects.filter(father_code=menu.menu_code,menu_level=2)
                if two_menu:
                    dict['menu_two'] =SFunSerializer(instance=two_menu,many=True).data
                    msgs.append(dict)
            return Response({"code": 200, "msgs": msgs})
        else:
            msgs = []
            dict =  {
            "menu_name": "订单系统",
            "menu_two": [
                {
                    "id": 2,
                    "menu_code": "M101",
                    "menu_name": "个人订单",
                    "url": "/user/personnel_order/",
                    "menu_level": "2",
                    "father_code": "M100",
                },
            ]
        },
            msgs.append(dict)
            return Response({"code": 200, "msgs": dict})


# 订单模块的增删改查
class Orders(viewsets.ModelViewSet):

    queryset = TheOrder.objects.all()
    serializer_class = OrderSerializer
    filter_class = RegionFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    pagination_class = PageViewSet


# 物流模块
class Tlog(viewsets.ModelViewSet):

    queryset = TLogCost.objects.all()
    serializer_class = TLogCostSerializer
    pagination_class = PageViewSet
    filter_class = tlogfilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)


# 订单模块人员
class Searchuser(viewsets.GenericViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientSerializer

    def list(self, request):
        receiving = Groupuser.objects.filter(group_name__contains='收货').first().id
        shipper = Groupuser.objects.filter(group_name__contains='发货').first().id
        yunshu = Groupuser.objects.filter(group_name__contains='运输').first().id

        receiving_list = ClientUser.objects.filter(group_id=receiving)
        shipper_list = ClientUser.objects.filter(group_id=shipper)
        yunshu_list = ClientUser.objects.filter(group_id=yunshu)


        msgs = {
            'shipper':ClientSerializer(instance=receiving_list,many=True).data,
            'receiving':ClientSerializer(instance=shipper_list,many=True).data,
            'transportation':ClientSerializer(instance=yunshu_list,many=True).data,
        }
        return Response({"code": 200, "msgs": msgs})
# 区域信息查询，。去重
class  Search_region(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = TLogCost.objects.all()
    serializer_class = TLogCostSerializer


    def list(self, request, *args, **kwargs):
        provinces = request.GET.get('provinces','')
        city = request.GET.get('city','')
        county = request.GET.get('county','')
        tounsty = request.GET.get('tounsty','')

        if provinces=='' and city=='' and county=='' and tounsty =='':
            new_list = []
            provinces_list = TLogCost.objects.all()
            for x in provinces_list:
                new_list.append(x.provinces)
            return Response({"code": 200, "msgs": set(new_list)})
        if provinces:
            new_list = []
            provinces_list = TLogCost.objects.filter(provinces=provinces)
            for x in provinces_list:
                new_list.append(x.city)
            return Response({"code": 200, "msgs": set(new_list)})
        if city:
            new_list = []
            provinces_list = TLogCost.objects.filter(city=city)
            for x in provinces_list:
                new_list.append(x.county)
            return Response({"code": 200, "msgs": set(new_list)})
        if county:
            new_list = []
            provinces_list = TLogCost.objects.filter(county=county)
            for x in provinces_list:
                new_list.append(x.tounsty)
            return Response({"code": 200, "msgs": set(new_list)})

# 导出excel
class Excel(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = TLogCost.objects.all()
    serializer_class = TLogCostSerializer


    def list(self, request, *args, **kwargs):
        array1 = []
        array2 = []
        array3 = []
        array4 = []
        array5 = []
        array6 = []
        type = request.GET.get('type')
        if type == 'seafoodTheorder':
            datas = TheOrder.objects.filter(type='其他')
            if datas:
                for data in datas:
                    array1.append(data.order_number)
                    array2.append(data.data_times)
                    array3.append(data.post_user)
                    array4.append(data.get_user)
                    array5.append(data.all_freight)
                    array6.append(data.type)
            df = pd.DataFrame({'订单号':array1,'时间':array2,'发货人':array3,'收货人':array4,'总金额':array5,'类型':array6})
            df.to_excel('static/seafoodTheorder.xlsx')
            return Response({'code':200,'msgs':'static/seafoodTheorder.xlsx'})

        if type == 'foodTheorder':
            datas = TheOrder.objects.filter(type='石材')
            if datas:
                for data in datas:
                    array1.append(data.order_number)
                    array2.append(data.data_times)
                    array3.append(data.post_user)
                    array4.append(data.get_user)
                    array5.append(data.all_freight)
                    array6.append(data.type)
            df = pd.DataFrame({'订单号': array1, '时间': array2, '发货人': array3, '收货人': array4, '总金额': array5, '类型': array6})
            df.to_excel('static/foodTheorder.xlsx')
            return Response({'code': 200, 'msgs': 'static/foodTheorder.xlsx'})
        if type =='all':
            return Response({'code': 200, 'msgs': '暂无功能'})
        if type =='user':
            datas = Userinfo.objects.all()
            if datas:
                for data in datas:
                    array1.append(data.username)
                    array2.append('是' if data.is_superadmin=='1' else '不是')
            df = pd.DataFrame({'用户名称': array1, '是否是管理员': array2})
            df.to_excel('static/user.xlsx')
            return Response({'code': 200, 'msgs': 'static/user.xlsx'})
        if type == '物流':
            datas = TLogCost.objects.all()
            if datas:
                for data in datas:
                    array1.append(data.provinces)
                    array2.append(data.city)
                    array3.append(data.county)
                    array4.append(data.tounsty)
                    array5.append(data.money)
            df = pd.DataFrame({'省份': array1, '城市': array2, '县': array3, '乡': array4, '费用': array5})
            df.to_excel('static/wuliu.xlsx')
            return Response({'code': 200, 'msgs': 'static/wuliu.xlsx'})


        else:
            return Response({'code': 200, 'msgs': '暂无功能'})
# 查询人员信息
class Search_User(viewsets.ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientSerializer
    filter_class = Search_user
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)


# 更新订单状态
class Update_Order(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = TheOrder.objects.all()
    serializer_class = UpdaorderSerializer


    def create(self, request, *args, **kwargs):
        id = request.POST.get('id')
        status = request.POST.get('status')

        order = TheOrder.objects.filter(id=id).first()
        order.status = status
        order.save()
        return Response({"code": 200, "msgs": '修改成功'})