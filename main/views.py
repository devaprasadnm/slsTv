from django.shortcuts import render
from .models import News
# Create your views here.

def home(request):
    news = News.objects.all()
    return(render(request,'main.html',{'news':news}))

