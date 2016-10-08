from django.shortcuts import render, redirect
from django.utils import http
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import login_required_message_and_redirect
from .models import Post
from .forms import ContactForm


def index(request):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        redirect_to = request.POST.get('next', request.GET.get('next', '/'))
        redirect_to = (redirect_to if http.is_safe_url(redirect_to, request.get_host()) else '/')
        login_user(request)
        return redirect(redirect_to)
    else:
        return render(request, 'blog/home.html')


def blog_view(request):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_user(request)
        return redirect(blog_view)
    else:
        return render(request, 'blog/blog.html', {'mylist': Post.objects.all().order_by("-date")})


def post_view(request, pk):
    if request.method == 'POST' and request.POST['login'] == 'Login':
        login_user(request)
        return redirect(post_view)
    else:
        return render(request, 'blog/post.html',
                      {'mypost': Post.objects.get(id=pk), 'mylist': Post.objects.all().order_by("-date")})


def contact_view(request):
    if request.method == 'POST':
        try:
            x = request.POST['login']
        except KeyError:
            x = None
        if x == 'Login':
            login_user(request)
            return redirect(contact_view)
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.success(request, 'Thank you for contacting, I will get back to you shortly!')
                return redirect(contact_view)
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


@login_required_message_and_redirect()
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
