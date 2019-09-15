from django.shortcuts import render
from .models import Post, Tag

def index(request):
    posts = Post.objects.all()
    return render(request, 'mainApp/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'mainApp/post_detail.html', context={'post': post})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainApp/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'mainApp/tag_detail.html', context={'tag': tag})