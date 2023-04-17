from django.shortcuts import render
from .models import Post
from django.views import generic

def home(request):
    return render(request, 'index.html')

def membros(request):
    return render(request, 'membros.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
