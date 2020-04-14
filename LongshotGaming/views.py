from django.shortcuts import render
from django.template import RequestContext

def page_not_found(request, exception=None):
    return render(request, 'LongshotGaming/404.html', {})

def server_error(request, exception=None):
    return render(request, 'LongshotGaming/503.html', {})