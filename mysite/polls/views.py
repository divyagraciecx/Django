from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
# displays the latest few questions.
#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index")
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    #context = {
        #'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
from django.http import Http404

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# displays a question text, with no results but with a form to vote.
#def detail(request, question_id):
    #return HttpResponse("You are looking at question %s." % question_id)

#displays results for a particular question.
def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

# handles voting for a particular choice in a particular question.
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
