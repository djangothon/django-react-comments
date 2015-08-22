from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from comment_react.models import Comments

@csrf_exempt
def home(request):
	context_instance=RequestContext(request)
	if request.method == 'GET':
		data = Comments.objects.all()
		return render_to_response('index.html', data)
	elif request.method == 'POST':
		data = request.POST.urlencode()
		comment = data.split('&')[0].split('=')[1]
		author = data.split('&')[1].split('=')[1]
		print 'comment - '+ comment
		print 'author - '+ author
		p1 = Comments(user_id=author,
			post_id = '1',
			comment = comment)
		p1.save()
		data = Comments.objects.all()
		return render_to_response('index.html', data)

def getComments(request):
	data = Comments.objects.all()
	print data
	# n = [e.encode('utf-8') for e in data.strip('[]').split(',')]
	# print n[0]
	return HttpResponse(data, content_type="application/json")


