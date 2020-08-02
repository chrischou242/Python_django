from django.shortcuts import render , HttpResponse , redirect
import random

def starting_gold(request):
    if not 'gold' in request.session:
        request.session['gold'] =0 
        request.session['counter']=0
    return render(request,"index.html")

def process_money(request):
    # request.session['counter'] +=1
    # if ( request)
    location = request.POST['location'] 
    if (location == "farm"):
        farm_gold = random.randint(10,20)
        request.session['gold'] += farm_gold
        print (farm_gold)
    elif (location =="cave"):
        farm_gold = random.randint(5,10)
        print (farm_gold)
        request.session['gold'] += farm_gold
    elif(location == "house"):
        farm_gold = random.randint(2,5)
        print (farm_gold)
        request.session['gold'] += farm_gold
    elif(location =='casino'):
        farm_gold = random.randint(-50,50)
        print (farm_gold)
        request.session['gold'] += farm_gold
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')


