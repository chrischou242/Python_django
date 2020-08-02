from django.urls import path
from .import views
urlpatterns = [
    path('',views.hi),
    path('/',views.root),
    path('blogs',views.index),
    path('blogs/new', views.new),
    path('blogs/<int:number>',views.show),
    path('blogs/<int:number>/edit',views.edit),
    path('blogs/<number>/delete', views.destroy),
    path('blogs/create', views.create),
]