from django.shortcuts import render
from django.http import HttpResponse

import datetime
# Create your views here.

def display(request):
    return HttpResponse("<h1>My First Django App!!</h1>")


def displayDateTime(request):    
    dt = datetime.datetime.now()
    s = "<b>Current date time is: </b>"+str(dt)
    return HttpResponse(s)


def renderMain(request):
    return render(request,"firstApp/index.html")


def renderPortfolioPage(request):
    return render(request,"firstApp/portfolio.html")


def renderBlogPage(request):
    return render(request,"firstApp/blog.html")

def renderContactPage(request):
    return render(request,"firstApp/contact.html")

