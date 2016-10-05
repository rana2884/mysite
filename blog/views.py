from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Post
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'blog/account.html')
            else:
                return render(request, 'blog/home.html', {'login_msg': "Your account is disabled"})
        else:
                return render(request, 'blog/home.html', {'login_msg': "Invalid login details"})
    else:
        return render(request, 'blog/home.html', {})


def blog(request):
    return render(request, 'blog/blog.html', {'mylist': Post.objects.all().order_by("-date")})


def post(request, pk):
    return render(request, 'blog/post.html', {'mypost': Post.objects.get(id=pk),'mylist': Post.objects.all().order_by("-date")})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = ContactForm()
            return render(request, 'blog/contact.html', {'form': form, 'thank': True})
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
