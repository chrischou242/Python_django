
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.hi),
    path('guess', views.guess),
    path('too_low',views.tooLow),
    path('too_high',views.tooHigh)
]
