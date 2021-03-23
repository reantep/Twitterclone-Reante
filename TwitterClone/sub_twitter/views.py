from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import tweet
from .forms import PictureForm
import datetime
from django.contrib import messages

from cloudinary.forms import cl_init_js_callbacks
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PictureForm()
    tweets = tweet.objects.all().order_by('-created_at')
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

def edit_tweet(request, id):
    template = 'sub_twitter/Edit-Tweet.html'
    post = get_object_or_404(tweet, pk=id)
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=post)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your tweet has been updated!')
        except Exception as e :
            messages.warning(request,'Your post was not saved:'.format(e))
    else:
        form = PictureForm(instance=post)
    ctx = {
        'form': form,
        'tweet': tweet,
        'post': post,
    }

    return render(request,template, ctx)
