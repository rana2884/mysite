from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return render(request, 'blog/home.html')


def blog(request):
    return render(request, 'blog/blog.html', {'blog_list': Post.objects.all().order_by("-date")})


def post(request, pk):
    return render(request, 'blog/post.html', {'blog_post': Post.objects.get(id=pk)})


def contact(request):
    return render(request, 'blog/contact.html')