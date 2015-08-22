from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from comment_react.models import Save_comments

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
		#models = Save_comments
		#comment = request.POST
		#comment.save()
		p1 = Save_comments(user_id=author,
			post_id = '1',
			comment = comment)
		p1.save()
		return render_to_response('index.html')

def comments_handler():

    with open('comments.json', 'r') as file:
        comments = json.loads(file.read())

    if request.method == 'POST':
        comments.append(request.form.to_dict())

        with open('comments.json', 'w') as file:
            file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})
