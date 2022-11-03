from django.urls import reverse

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from . models import Question,Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        dct = {'question':question,'error_message':"You forgot to select a choice."}
        return render(request,'polls/detail.html',dct)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print(selected_choice)

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''def index(request):
    latest_5_Q_list = Question.objects.order_by('-pub_date')[:4]
    context = {'latest_question_list': latest_5_Q_list}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})'''



