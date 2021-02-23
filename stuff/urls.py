from django.urls import path
from . import views

urlpatterns = [
               path('astro', views.AstroView, name='astro'),
               path('download', views.DownloadView, name='download'),
               path('vim', views.VimView, name='vim'),
               path('photo', views.PhotoView, name='photo'),
               path('f1', views.F1View, name='f1'),
              ]
