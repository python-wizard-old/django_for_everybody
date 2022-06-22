from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view():
	return HttpResponse("Hello, world. 0b6cf75f is the polls owner.")