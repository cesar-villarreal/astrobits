from django.shortcuts import render
from .models import Picture, Drivers, Constructors, Driverstandings
import requests
from bs4 import BeautifulSoup
from .functions.f1Dash import dnats, cnats, driver_position
from bokeh.embed import components
from bokeh.layouts import row
#from django.http import HttpResponse

def AstroView(request):
	title = "Astro"
	return render(request, 'astro.html', {'title': title})

def DownloadView(request):
	url = "http://cvillarreal.xyz/astrobits/stuff/download"
	response_text = requests.get(url, params={}).text
	links_delete = 5
	soup = BeautifulSoup(response_text, 'html.parser')
	a = soup.find_all('a')
	files_list = [url+'/'+i.get('href') for i in a]
	for i in range(links_delete):
		del files_list[0]

	title = "Download"
	return render(request, 'download.html', {'title': title,
		'files_list': files_list})

def VimView(request):
	title = "VIM"
	return render(request, 'vim.html', {'title': title,})

def PhotoView(request):
	title = "Photography"
	pictures = Picture.objects.all()
	return render(request, 'photo.html', {'title': title,
                                          'pictures': pictures})

def F1View(request):
	title = "F1 Statistics"

	plot_dnats = dnats(Drivers)
	plot_cnats = cnats(Constructors)
	plot_driver_position = driver_position(Drivers, Driverstandings)
	
	script_nats, div_nats = components(row(plot_dnats, plot_cnats),
                                       theme = 'dark_minimal')
	script_driver, div_driver = components(plot_driver_position,
                                           theme = 'dark_minimal')
	
	return render(request, 'f1.html', {'script_nats': script_nats,
									   'div_nats': div_nats,
									   'script_driver': script_driver,
									   'div_driver': div_driver})
