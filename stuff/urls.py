from django.urls import path
from . import views

urlpatterns = [
               path('stuff', views.StuffsView, name='index'),
              ]