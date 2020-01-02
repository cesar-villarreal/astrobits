from django.shortcuts import render
from django.http import HttpResponse
from stuff.files_list import GetFilesList

def AstroView(request):
	title = "Astro"
	return render(request, 'astro.html', {'title': title, })

def DownloadView(request):
	title = "Download"
	files_list = GetFilesList
	return render(request, 'download.html', {'title': title,
                                          'files_list': files_list})
