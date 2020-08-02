from django.urls import path
from . import views

urlpatterns =[
    path('', views.forms),
    path('survey',views.create_survey),
    path('hi',views.some_function)
]