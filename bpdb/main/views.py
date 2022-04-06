from django.shortcuts import render
from .models import Notice, Update

# Create your views here.

def home(request):
    notice = Notice.objects.all().order_by('-id')
    return render(request, 'main/home.html', {'notice': notice})


def updates(request):
    update = Update.objects.all().order_by('-id')
    return render(request, 'main/update.html', {'update': update})