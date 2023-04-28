from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment, Blogger
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from blog.forms import PostBlog, PostComment
import datetime

class BlogListView(generic.ListView):
    model = Post
    context_object_name = 'blog_list'
    template_name = 'blog/templates/blog_list.html'
    paginate_by = 5

class BloggerListView(generic.ListView):
    model = Blogger
    template_name = 'blog/templates/blogger_list.html'

def post_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'blog/post_detail.html', context={'post': post})

class BloggerDetailView(generic.DetailView):
    model = Blogger

@login_required
def profiles_view(request):
    # user = request.GET['User.username']
    # b_q = Blogger.objects.filter(username__exact=user).counts()
    # # context = {'usern': user}
    # # User.objects.filter(id__exact=user_id)
    # if b_q != 1:
    #     context = {'usern': user, 'blogger': False}
    # else:
    #     blogger = Blogger.objects.filter(username__exact=user)
    #     context = {'usern': user, 'blogger': blogger}
    return render(request, 'profile.html')

class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'blog/user_form.html'
    success_url = reverse_lazy('home')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'blog/user_confirm_delete.html'
    success_url = reverse_lazy('home')

@login_required
@permission_required('blog.can_post', raise_exception=True)
def post_blog(request):
    if request.method == 'POST':
        form = PostBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.blogger
            post.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostBlog()

    context = {
        'form': form,
        }

    return render(request, 'blog/new_post.html', context)

@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=((pk,))))
    else:
        form = PostComment()

    context = {
        'form': form,
        'post': post,
        }

    return render(request, 'blog/new_comment.html', context)

class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    model = Comment
    # self.pk = pk
    # comment = get_object_or_404(Comment, pk=self.pk)
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('home')
    # success_url = reverse('post-detail', args=((comment.post.pk,)))
    permission_required = 'blog.can_delete_comment'
