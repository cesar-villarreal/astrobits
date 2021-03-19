from django.shortcuts import render
from .models import Picture, Drivers, Constructors, Driverstandings
from .forms import julianDateForm, dateJulianForm
import requests

from bs4 import BeautifulSoup
from bokeh.embed import components
from bokeh.layouts import row
from .functions.f1Dash import dnats, cnats, driver_position
from .functions.jd import date_jd, jd_date



def AstroView(request):
	title = "Astro"
	julian_date_form = julianDateForm()
	date_julian_form = dateJulianForm()
	
	
	if request.method == 'POST':

		if request.POST.__contains__('julian_form'):
			print('julian form')
			to_jd = request.POST['julian_form']
			julian_date = date_jd(to_jd)
			
			return render(request, 'astro.html', {'title': title,
                                                  'julian_date_form': julian_date_form,
                                                  'date_julian_form': date_julian_form,
                                                  'julian_date': julian_date})

		if request.POST.__contains__('date_form'):
			print('date form')
			to_date = float(request.POST['date_form'])
			date_julian = jd_date(to_date)
		
			return render(request, 'astro.html', {'title': title,
                                                  'julian_date_form': julian_date_form,
                                                  'date_julian_form': date_julian_form,
                                                  'date_julian': date_julian})
		
	return render(request, 'astro.html', {'title': title,
									      'julian_date_form': julian_date_form,
									      'date_julian_form': date_julian_form})

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
	title = "F1"

	plot_dnats = dnats(Drivers)
	plot_cnats = cnats(Constructors)
	
	script_nats, div_nats = components(row(plot_dnats, plot_cnats),
                                       theme = 'dark_minimal')
	script_position, div_position = driver_position(Drivers, Driverstandings)

	return render(request, 'f1.html', {'title': title,
									   'script_nats': script_nats,
									   'div_nats': div_nats,
									   'script_position': script_position,
									   'div_position': div_position,
									   })
