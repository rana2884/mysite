from django.shortcuts import render
from core.decorators import login_required_message_and_redirect


@login_required_message_and_redirect
def index(request):
    return render(request, 'dashboard/base.html')