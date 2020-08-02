from django.shortcuts import render, HttpResponse, redirect

def counter(request):
    if not 'count' in request.session:
        request.session['count'] = 1    
    
    else:
        request.session['count'] +=1
    
    return render(request, "index.html")


def delete(request):
    request.session.clear()
    return redirect('/')