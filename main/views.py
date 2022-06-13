from django.shortcuts import render
from .models import News,Images
# Create your views here.

def home(request):
    news = News.objects.all()
    images = Images.objects.all()
    return(render(request,'main.html',{'news':news,'images':images}))

