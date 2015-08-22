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
		print request.POST
		comment = request.POST
		comment.save()
		return render_to_response('index.html')

def comments_handler():

    with open('comments.json', 'r') as file:
        comments = json.loads(file.read())

    if request.method == 'POST':
        comments.append(request.form.to_dict())

        with open('comments.json', 'w') as file:
            file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})