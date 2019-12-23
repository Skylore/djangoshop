from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', context={'posts': posts})

def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'post_details.html', context={'post': post})
