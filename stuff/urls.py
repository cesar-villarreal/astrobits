from django.urls import path
from . import views

urlpatterns = [
               path('astro', views.AstroView, name='astro'),
              ]
