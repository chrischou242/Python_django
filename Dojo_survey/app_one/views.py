from django.shortcuts import render, HttpResponse


def forms(request):
    return render(request,"index.html")

def create_survey(request):
    print("Got post from info......")
    name_from_survey = request.POST['name']
    location_from_survey = request.POST['location']
    language_from_survey = request.POST['language']
    context ={
        "name_on_survey": name_from_survey,
        "location_on_survey" : location_from_survey,
        "language_on_survey":language_from_survey
    }
    return render(request,"show.html",context)

def some_function(request): 
    request.session['name']= request.POST['name']
    request.session['counter'] = 100

    return render(request,"index.html")
