from django.shortcuts import render
from .models import Picture, Drivers
import requests
from bs4 import BeautifulSoup
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.transform import cumsum
from bokeh.palettes import inferno

from pandas import DataFrame
from math import pi


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
	
	nationalities = Drivers.objects.using('f1').raw('SELECT driverId,\
		nationality, COUNT(*) as n_nat FROM drivers GROUP BY nationality')
	nationalities = DataFrame([item.__dict__ for item in nationalities])\
		.drop(columns=['_state','driverid'])
	nationalities['angle'] = nationalities['n_nat']/nationalities['n_nat']\
		.sum()*2*pi
	nationalities['color'] = list(inferno(41))
	
	plot = figure(plot_height=350,
		title="F1 Nationalities",
		#toolbar_location=None,
		tools="hover",
		tooltips="@nationality: @n_nat",
		x_range=(-0.5, 1.0))
	plot.wedge(x=0, y=1,
		radius=0.3,
		start_angle=cumsum('angle', include_zero=True),
		end_angle=cumsum('angle'),
		line_color = 'white',
		fill_color = 'color',
		legend_field = 'nationality',
		source = nationalities)
	script, div = components(plot)

	#x = [0,1,2,3,4]
	#y = [0,1,2,3,4]
	#plot = figure(title='test', x_axis_label='x', y_axis_label='y',\
		#plot_width=400, plot_height=400)
	#plot.line(x,y,line_width=2)
	#script, div = components(plot)
	
	return render(request, 'f1.html', {'script': script, 'div': div})
