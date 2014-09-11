from django.shortcuts import render
from django.http import HttpResponse

def current_url(request):
    return HttpResponse("the url is %s" % request.get_host())
