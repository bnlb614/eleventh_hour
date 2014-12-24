from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic 

from polls.models import Question, Choice

# def index(request):
# 	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	# context = RequestContext(request, {'latest_question_list': latest_question_list,
# 	# 	})
# 	# return HttpResponse(template.render(context))
# 	#or 
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list':latest_question_list}
# 	return render(request, 'polls/index.html',context)


# def detail(request,question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404
# 	return render(request, 'polls/detail.html', {'question':question})
# 	# return HttpResponse("You're looking at questions {}".format(question_id))

# def results(request,question_id):
# 	question = get_object_or_404(Question, pk=question_id) #same as try/except above
# 	return render(request, 'polls/results.html', {'question':question})


	# return HttpResponse("You're voting on question {}".format(question_id))

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request,question_id):
	p = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question':p,
			'error_message': "You didn't select a choice."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))









