
#导入第三方的模块
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import mixins,generics
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler



# 导入自定义封装的方法
from .utils import MyPermission,MyAuthentication
from tools.get_ip import client_ip
from .serializers import CreateUserSerializer,RegisterSerializer,GroupuserSerializer
from tools.newpage import PageViewSet

# 导入model
from .models import  Userinfo,Groupuser
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
                        return Response({"code":200,"token":token,'username':uesr_query.username})
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


