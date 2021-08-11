from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    Message = " Hi! Welcome to the innovation with python training."
    return render(response,'FIRSTPROJECT/index.html',context = {'Messsage':Message})
