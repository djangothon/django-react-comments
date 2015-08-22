from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
	context_instance=RequestContext(request)
	print request
	if request.method == 'GET':
		return render_to_response('index.html')
	elif request.method == 'POST':
		data = request.POST.urlencode()
		comment = data.split('&')[0].split('=')[1]
		author = data.split('&')[1].split('=')[1]
		print 'comment - '+ comment
		print 'author - '+ author
		# Save author and comment to db
		return render_to_response('index.html')
