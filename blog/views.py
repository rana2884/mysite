from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'blog/home.html')


def blog(request):
    return render(request, 'blog/blog.html', {'mylist': Post.objects.all().order_by("-date")})


def post(request, pk):
    return render(request, 'blog/post.html', {'mypost': Post.objects.get(id=pk),'mylist': Post.objects.all().order_by("-date")})


def contact(request):
    return render(request, 'blog/contact.html')