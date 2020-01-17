


# 定义拦截到ip的方法
def client_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]
        return client_ip
    else:
        client_ip = request.META['REMOTE_ADDR']
        return client_ip