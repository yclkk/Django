from django.http import HttpResponse

def index(request):
    return HttpResponse("这是第一个页面")
