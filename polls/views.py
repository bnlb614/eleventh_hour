from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from polls.models import Question, Choice

def index(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = RequestContext(request, {'latest_question_list': latest_question_list,
	# 	})
	# return HttpResponse(template.render(context))
	#or 
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request, 'polls/index.html',context)


def detail(request,question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'question':question})
	# return HttpResponse("You're looking at questions {}".format(question_id))

def results(request,question_id):
	return HttpResponse('You\'re looking at the results of question {}'.format(question_id))

def vote(request,question_id):
	return HttpResponse("You're voting on question {}".format(question_id))