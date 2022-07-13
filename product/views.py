from tkinter import N
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(*args,**kwargs):
    return HttpResponse("<h1> this is home page</h1>")


def about(request,*args,**kwargs):
    my_context={
        "my_text" : "my name is sammy",
        "my_numb" : 9867867202,
        "my_context": [123,456,789,1011,1213]

    }
    return render(request, "about.html", my_context)


def contact(request,*args,**kwargs):
     return render(request, "contact.html", {})