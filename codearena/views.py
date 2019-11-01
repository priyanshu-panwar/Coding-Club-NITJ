from django.shortcuts import render, get_object_or_404, redirect
from .models import Coding_Profile, Question, Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SolutionForm
from django.utils import timezone

def home(request):
    posts = Event.objects.all()
    posts = posts[::-1]
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'codearena/home.html', context)

def post_detail(request, pk):
    object = get_object_or_404(Event, pk=pk)
    now = timezone.now
    validity = False
    if object.date_valid>=timezone.now():
    	validity = True
    if request.method == 'POST':
        comment_form = SolutionForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.coder = request.user
            new_comment.event = object
            new_comment.save()
            return render(request, 'codearena/thanks.html')
            
    else:
        comment_form = SolutionForm()

    return render(request, 'codearena/post_detail.html', {'object': object, 'comment_form': comment_form, 'validity': validity,})
