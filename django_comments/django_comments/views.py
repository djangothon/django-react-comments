from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from comment_react.models import Save_comments

@csrf_exempt
def home(request):
	context_instance=RequestContext(request)
	print request
	if request.method == 'GET':
		comments_all = Save_comments.objects.all()
		print comments_all
		return render_to_response('index.html')
	elif request.method == 'POST':
		data = request.POST.urlencode()
		comment = data.split('&')[0].split('=')[1]
		author = data.split('&')[1].split('=')[1]
		print 'comment - '+ comment
		print 'author - '+ author
		p1 = Save_comments(user_id=author,
			post_id = '1',
			comment = comment)
		p1.save()
		return render_to_response('index.html')
