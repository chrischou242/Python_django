from django.shortcuts import render

def hi(request):
    return render(request, "index.html")

# Create your views here.
