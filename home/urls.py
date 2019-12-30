from django.urls import path
from . import views

urlpatterns = [
               path('', views.indexView, name='index'),
               path('home/about', views.aboutView, name='about'),
              ]