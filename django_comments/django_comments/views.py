from django.shortcuts import render, render_to_response
from django.template import RequestContext

def home(request):
	context_instance=RequestContext(request)
	print request
	if request.method == 'GET':
		return render_to_response('index.html')
	elif request.method == 'POST':
		print 'out'
		return render_to_response('index.html')

def post():
	print 'in'
