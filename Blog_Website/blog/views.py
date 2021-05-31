from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView,
                                        CreateView,
                                        UpdateView,
                                        DeleteView)
from .models import Post
from django.http import HttpResponse

def home(request):
    template_name = loader.get_template('blog/home.html')

    context = {
        'posts' : Post.objects.all()
    }

    return HttpResponse(template_name.render(context, request))
    
    # return render(request,'blog/home.html' , context)

    # return HttpResponse('<h1> Blog Home </h1>')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewType>.html  
    context_object_name = 'posts'
    ordering = ['-date'] 
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  #<app>/<model>_<viewType>.html  
    context_object_name = 'posts'
    # ordering = ['-date'] 
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):  # Override method
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):  # Override method
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author) :
            return True
        return False    
       # return super().test_func()    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/blog'
    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author) :
            return True
        return False  


def about(request):
     return render(request,'blog/about.html', {'title' : 'About'} )

