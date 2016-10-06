from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post
from .forms import ContactForm


def index(request):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_user(request)
        return redirect(index)
    else:
        return render(request, 'blog/home.html')


def blog(request):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_user(request)
        return redirect(blog)
    else:
        return render(request, 'blog/blog.html', {'mylist': Post.objects.all().order_by("-date")})


def post(request, pk):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_user(request)
        return redirect(post)
    else:
        return render(request, 'blog/post.html', {'mypost': Post.objects.get(id=pk),'mylist': Post.objects.all().order_by("-date")})


def contact(request):
    if request.method == 'POST':
        try:
            x = request.POST['login']
        except KeyError:
            x = None
        if x == 'Login':
            login_user(request)
            return redirect(contact)
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.success(request, 'Thank you for contacting, I will get back to you shortly!')
                return redirect(contact)
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def logout_view(request):
        logout(request)
        messages.error(request, 'You have been logged out!')
        return redirect(index)


# Helper function
def login_user(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You are logged in!')
            else:
                messages.warning(request, 'Your account is disabled!')
        else:
            messages.error(request, 'Invalid login details')


