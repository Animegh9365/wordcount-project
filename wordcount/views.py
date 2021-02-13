from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homepage.html')

def count(request):
    Your_text=request.GET['TEXT']

    word_list=Your_text.split()

    return render(request,'count.html',{'Full_text':Your_text,'count':len(word_list)})
