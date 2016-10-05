from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Post
from .forms import ContactForm


def index(request):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_msg = login_user(request)
        return render(request, 'blog/home.html', {'login_msg': login_msg})
    else:
        return render(request, 'blog/home.html', {})


def blog(request):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_msg = login_user(request)
        return render(request, 'blog/blog.html', {'login_msg': login_msg, 'mylist': Post.objects.all().order_by("-date")})
    else:
        return render(request, 'blog/blog.html', {'mylist': Post.objects.all().order_by("-date")})


def post(request, pk):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_msg = login_user(request)
        return render(request, 'blog/post.html', {'login_msg': login_msg, 'mypost': Post.objects.get(id=pk), 'mylist': Post.objects.all().order_by("-date")})
    else:
        return render(request, 'blog/post.html', {'mypost': Post.objects.get(id=pk),'mylist': Post.objects.all().order_by("-date")})


def contact(request):
    if request.method == 'POST':
        form = ContactForm()
        try:
            x = request.POST['login']
        except KeyError:
            x = None
        if x == 'Login':
            login_msg = login_user(request)
            return render(request, 'blog/contact.html', {'login_msg': login_msg, 'form': form})
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                form = ContactForm()
                return render(request, 'blog/contact.html', {'form': form, 'thank': True})
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def logout_view(request):
        logout(request)
        return redirect(index)


# Helper function
def login_user(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                msg = ""
            else:
                msg = "Your account is disabled"
        else:
            msg = "Invalid login details"
        return msg
