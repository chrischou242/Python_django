
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.starting_gold),
    path('process_money',views.process_money),
    path('reset',views.reset)
]

