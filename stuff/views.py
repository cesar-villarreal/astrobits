from django.shortcuts import render
#from django.http import HttpResponse

def AstroView(request):
	title = "Astro"
	return render(request, 'astro.html', {'title': title, })

def DownloadView(request):
	from stuff.files_list import GetFilesList
	title = "Download"
	return render(request, 'download.html', {'title': title,
                                             'files_list': GetFilesList})

def VimView(request):
	title = "VIM"
	return render(request, 'vim.html', {'title': title,})

def PhotoView(request):
	title = "Photography"
	return render(request, 'photo.html', {'title': title})