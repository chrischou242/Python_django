from django.shortcuts import render, redirect , HttpResponse
import random 
ranom_number = random.randint(1,100)


def hi(request):
    return render(request, "index.html")

def guess(request):
    request.session['count'] = ranom_number
    print (request.session['count'])
    number_guessed = request.POST['guess']
   
    
    if (int(number_guessed)<int(request.session['count'])):
        return render(request,"too_low.html")
    elif(int(number_guessed) > int(request.session['count'])):
        return render(request, "too_high.html")
    elif(int(number_guessed) == int(request.session['count'])):
        return render(request, "you_win.html" )

def tooLow(request):
    return redirect('/')

def tooHigh(request):
    return redirect('/')