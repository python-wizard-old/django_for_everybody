from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
	num_visits = request.session.get('num_visits', 0) + 1
	request.session['num_visits'] = num_visits

	if num_visits > 4:
		del (request.session['num_visits'])

	resp = HttpResponse('7b4f363a view count=' + str(num_visits))
	resp.set_cookie('dj4e_cookie', '7b4f363a', max_age=1000)

	return resp