from django.shortcuts import render
from .models import News,Images
from django.http import JsonResponse
# Create your views here.

def home(request):
    return (render(request,'main.html'))


def data(request):
    news = News.objects.all()
    images = Images.objects.all()
    return JsonResponse({"users": list(news.values()),"image":list(images.values())})