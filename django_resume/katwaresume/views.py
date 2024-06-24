from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'katwaresume/resume_1.html')


def about(request):
    return HttpResponse('<h1>This is the about page</h1>')

# Create your views here.
