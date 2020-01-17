from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from  . import views
from rest_framework.documentation import include_docs_urls


API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'
# 定义路由地址
router  = routers.DefaultRouter()
# 注册新的路由地址
router.register(r'login', views.Login,basename=u'用户登录')   #  用户登录获取token
router.register(r'register', views.Register,basename=u'用户注册')   # 用户注册页面
router.register(r'group', views.Group,basename=u'用户组')   #  用户组信息
router.register(r'customer',views.Customer,basename='客户模块') # 客户信息
router.register(r'sfunmsgs',views.SFunMsg,basename='导航栏')      # 升级日志
router.register(r'theorder',views.Orders,basename='订单模块')
router.register(r'tlog',views.Tlog,basename='物流模块')

urlpatterns = [
    path('', include(router.urls)),
    # path(r'docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, authentication_classes=[], permission_classes=[])),
]
urlpatterns += router.urls