from django_filters import rest_framework as filters
from .models import  TheOrder


# # 查询
class RegionFilter(filters.FilterSet):
    post_user = filters.CharFilter(field_name='post_user',lookup_expr='icontains')
    get_user = filters.CharFilter(field_name='get_user',lookup_expr='icontains')
    the_party1 = filters.CharFilter(field_name='the_party1',lookup_expr='icontains')
    the_party2 = filters.CharFilter(field_name='the_party2',lookup_expr='icontains')
    data_times = filters.CharFilter(field_name='data_times',lookup_expr='icontains')
    order_number = filters.CharFilter(field_name='order_number',lookup_expr='icontains')

    class Meta:
        model = TheOrder
        fields = ['post_user','get_user','the_party1','the_party2','data_times','order_number']

