from django.shortcuts import render
from .models import News,Images
from django.http import JsonResponse
# Create your views here.

def index(request):
    pics = Images.objects.all()
    return (render(request,'index.html',{'pics':pics}))

def data_index(request):
    news = News.objects.all()
    pics = Images.objects.all()


    return JsonResponse({"users": list(news.values()),"image":list(pics.values())})