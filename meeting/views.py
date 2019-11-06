from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.utils import timezone
from django.views import generic
import datetime
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm

@login_required
def add_question(request):
    if request.method == 'POST':
        u_form = QuestionForm()
        if u_form.is_valid():
            u_form.save(commit=False)
            u_form.author = request.user
            u_form.save()
            return redirect('meeting:index')
    else:
        u_form = QuestionForm()
        
    context = {
        'u_form': u_form,
    }

    return render(request, 'meeting/add.html', context)
    

class IndexView(generic.ListView):
    template_name = 'meeting/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'meeting/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'meeting/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if 1==0: #question.date_valid<=timezone.now():
        return render(request, 'meeting/results.html question.id', {'error_message': "The Question is no longer available for voting."})
    else:
        question.hits+=1
        question.save()
        return HttpResponseRedirect(reverse('meeting:results',args=(question.id,)))
