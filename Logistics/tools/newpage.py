from rest_framework.pagination import PageNumberPagination
# 分页
class PageViewSet(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_query_param = 'p'
    page_size_query_param = 'page_size'




class TlogPageViewSet(PageNumberPagination):
    page_size = 3000
    max_page_size = 3000
    page_query_param = 'p'
    page_size_query_param = 'page_size'