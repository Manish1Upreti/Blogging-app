from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# posts = [
#     {
#           'author': 'Manish',
#            'title': 'Blog post 1',
#            'content': 'First post Content',
#             'date_posted': 'May 27, 2020'
#     },
# {
#           'author': 'Anish',
#            'title': 'Blog post 2',
#             'content': 'Second post Content',
#             'date_posted': 'May 28, 2020'
#     },
# {
#           'author': 'Abash',
#            'title': 'Blog post 3',
#             'content': 'Third post Content',
#             'date_posted': 'May 29, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'home'
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

# for giving the user who is posting blog
    # method is form_valid and self and form as an arguments
    def form_valid(self, form):
        form.instance.author = self.request.user  # current form author is current login user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

# for giving the user who is posting blog
    # method is form_valid and self and form as an arguments
    def form_valid(self, form):
        form.instance.author = self.request.user  # current form author is current login user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:    # to check if the current user is the author of the post , it prevent updating other user post
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:    # to check if the current user is the author of the post , it prevent updating other user post
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
