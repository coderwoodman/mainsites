from django.shortcuts import render_to_response

def index(request):
    currenthost=request.get_host()
    return render_to_response('index.html',{'currenthost':currenthost})

def about(request):
    currenthost=request.get_host()
    return render_to_response('about.html',{'currenthost':currenthost})
