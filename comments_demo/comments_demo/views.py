from django.shortcuts import render, render_to_response

def home(request):
	print request
	if request.method == 'POST':
		print 'in'
		return render_to_response('demo.html')
	else:
		return render_to_response('demo.html')
