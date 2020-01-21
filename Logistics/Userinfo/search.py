from django_filters import rest_framework as filters
from .models import  TheOrder,TLogCost,ClientUser


# # 查询
class RegionFilter(filters.FilterSet):
    post_user = filters.CharFilter(field_name='post_user',lookup_expr='icontains')
    get_user = filters.CharFilter(field_name='get_user',lookup_expr='icontains')
    the_party1 = filters.CharFilter(field_name='the_party1',lookup_expr='icontains')
    the_party2 = filters.CharFilter(field_name='the_party2',lookup_expr='icontains')
    data_times = filters.CharFilter(field_name='data_times',lookup_expr='icontains')
    # order_number = filters.CharFilter(field_name='order_number',lookup_expr='icontains')
    type = filters.CharFilter(field_name='type',lookup_expr='icontains')

    class Meta:
        model = TheOrder
        fields = ['post_user','get_user','the_party1','the_party2','data_times','order_number','type']

class tlogfilter(filters.FilterSet):
    provinces = filters.CharFilter(field_name='provinces', lookup_expr='icontains')
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')
    county = filters.CharFilter(field_name='county', lookup_expr='icontains')
    tounsty = filters.CharFilter(field_name='tounsty', lookup_expr='icontains')


    class Meta:
        model = TLogCost
        fields = ['provinces','city','county','tounsty']


class Search_user(filters.FilterSet):
    client_name = filters.CharFilter(field_name='client_name', lookup_expr='icontains')


    class Meta:
        model = ClientUser
        fields = ['client_name','group_id']

