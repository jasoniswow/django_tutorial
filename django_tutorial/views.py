from django.http import HttpResponse
from django.shortcuts import render # render HTML template

# create webpages

def homepage(request):
    #return HttpResponse('This is the homepage')
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('Nothing here')
    return render(request,'about.html')
