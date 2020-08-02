from django.urls import path
from .import views

urlpatterns = [
    path('',views.counter),
    path('delete',views.delete),
   
]
