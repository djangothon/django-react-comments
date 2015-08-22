from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from comment_react.models import Comments

@csrf_exempt
def home(request):
	context_instance=RequestContext(request)
	if request.method == 'GET':
		data = Comments.objects.all()
		comments = []
		for obj in data:
			commentCurr = {
			"user_id": obj.user_id,
			"comment": obj.comment,
			"post_id": obj.post_id,
			}
			comments.append(commentCurr)
		return render_to_response('index.html', comments)
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
		comments = []
		for obj in data:
			commentCurr = {
			"user_id": obj.user_id,
			"comment": obj.comment,
			"post_id": obj.post_id,
			}
			comments.append(commentCurr)
		return render_to_response('index.html', comments)

def getComments(request):
	data = Comments.objects.all()
	comments = []
	for obj in data:
		commentCurr = {
		"user_id": obj.user_id,
		"comment": obj.comment,
		"post_id": obj.post_id,
		}
		comments.append(commentCurr)
	print comments
	return render_to_response('index.html',comments)


