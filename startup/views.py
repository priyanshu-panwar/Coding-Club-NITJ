from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, Comment_Idea
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy


def home(request):
    posts = Idea.objects.all()
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
    return render(request, 'startup/home.html', context)

def post_detail(request, pk):
    object = get_object_or_404(Idea, pk=pk)
    comments = object.comments_idea.filter(Parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment_Idea.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = object
            new_comment.author = request.user
            new_comment.save()
            return redirect('startup:post-detail', object.id)
            
    else:
        comment_form = CommentForm()


    return render(request, 'startup/post_detail.html', {'object': object, 'comments': comments, 'comment_form': comment_form})

@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        form.save_m2m()
        # message success
        #messages.success(request, "Successfully Created")
        return redirect('startup:home')
    context = {
        "form": form,
    }
    return render(request, "startup/post_form.html", context)

class UserPostListView(ListView):
    model = Idea
    template_name = 'startup/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    fields = ['title', 'content']
    success_url = reverse_lazy('startup:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.author:
            return True
        return False

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Idea, pk=pk)
    post.delete()
    return redirect('startup:home')
