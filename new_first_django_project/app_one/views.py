from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def hi(request):
    return HttpResponse("")

def root(request):
    return redirect("/")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")



def show(request,number):
    return HttpResponse("plaeholder to display blog number" + str(number))


def edit(request,number):
    return HttpResponse("placeholder to edit blog" + str(number) )    

def destroy(request,number):
    return redirect("/blogs")

def create(request):
    return redirect("/")

