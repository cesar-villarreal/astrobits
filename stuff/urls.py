from django.urls import path
from . import views

urlpatterns = [
               path('astro', views.AstroView, name='astro'),
               path('download', views.DownloadView, name='download'),	
               path('vim', views.VimView, name='vim'),
              ]
