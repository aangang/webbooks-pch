from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def aaa(request):
    return HttpResponse('hello')