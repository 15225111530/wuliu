from rest_framework.pagination import PageNumberPagination




class VideoPagination(PageNumberPagination):
    page_size = 10     # 默认每页显示的条数
    page_size_query_param ='page_size'    # 自己输入每页的页码数
    page_query_param = "p"