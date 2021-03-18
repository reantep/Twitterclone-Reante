from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tweet
from .forms import PictureForm
from datetime import datetime

from cloudinary.forms import cl_init_js_callbacks


def dashboard(request):
    return HttpResponse('hello')

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PictureForm()
    tweets = tweet.objects.all()
    ctx = {'tweets': tweets, 'form': form }
    return render(request, 'sub_twitter/home.html', ctx)

def loadPicture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PictureForm()
    ctx = {'form': form}
    return render(request, 'sub_twitter/Post-tweet.html', ctx )