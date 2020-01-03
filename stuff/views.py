from django.shortcuts import render
from stuff.files_list import GetFilesList
#from django.http import HttpResponse

def AstroView(request):
	title = "Astro"
	return render(request, 'astro.html', {'title': title, })

def DownloadView(request):
	title = "Download"
	files_list = GetFilesList
	return render(request, 'download.html', {'title': title,
                                             'files_list': files_list})

def VimView(request):
	title = "VIM"
	return render(request, 'vim.html', {'title': title,})