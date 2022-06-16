from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. 68a82266 is the polls index.")
