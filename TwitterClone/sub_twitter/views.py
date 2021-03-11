from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tweet
from .forms import PictureForm

from cloudinary.forms import cl_init_js_callbacks


def dashboard(request):
    return HttpResponse('hello')

# Create your views here.
def index(request):
    image = tweet.objects.all()
    ctx = {'image': image }
    return render(request, 'sub_twitter/index.html', ctx)

def loadPicture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = PictureForm()
    ctx = {'form': form}
    return render(request, 'sub_twitter/load.html', ctx )