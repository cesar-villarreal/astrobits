from django.shortcuts import render
from .models import Picture, Drivers, Constructors

import requests

from bs4 import BeautifulSoup

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.transform import cumsum
from bokeh.palettes import viridis 

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
	
	dnats = Drivers.objects.using('f1').raw('SELECT driverId,\
		nationality, COUNT(nationality) AS n_nat FROM drivers\
		GROUP BY nationality ORDER BY n_nat')
	dnats = DataFrame([item.__dict__ for item in dnats])\
		.drop(columns=['_state','driverid'])
	dnats['percent'] = 100*(dnats['n_nat']/\
		dnats['n_nat'].sum())
	dnats['angle'] = dnats['n_nat']/dnats['n_nat']\
		.sum()*2*pi
	dnats['color'] = list(viridis(41))
	
	plot_dnats = figure(plot_height = 300,
		plot_width = 300,
		title = "F1 Drivers Nationalities",
		toolbar_location = None,
		tools = "hover",
		tooltips = "@nationality: @n_nat, @percent%",
		x_range = (-1.0, 1.0))
	
	plot_dnats.xaxis.visible = False
	plot_dnats.yaxis.visible = False
	plot_dnats.xgrid.visible = False
	plot_dnats.ygrid.visible = False
	plot_dnats.background_fill_color = 'black'
	#plot.toolbar.autohide = True
	#plot.sizing_mode = "scale_width"
	
	plot_dnats.wedge(x = 0, y = 0,
		radius = 0.9,
		start_angle = cumsum('angle', include_zero = True),
		end_angle = cumsum('angle'),
		line_color = 'black',
		fill_color = 'color',
		#legend_field = 'nationality',
		source = dnats)
	script_dnats, div_dnats = components(plot_dnats)
	
	cnats = Constructors.objects.using('f1').raw('SELECT constructorId,\
		nationality, COUNT(nationality) AS n_nat FROM constructors\
		GROUP BY nationality ORDER BY n_nat DESC')
	cnats = DataFrame([item.__dict__ for item in cnats]).drop(columns=['_state'])
	cnats['percent'] = 100*(cnats['n_nat']/\
	cnats['n_nat'].sum())
	cnats['angle'] = cnats['n_nat']/cnats['n_nat']\
		.sum()*2*pi
	cnats['color'] = list(viridis(24))
	
	plot_cnats = figure(plot_height = 300,
		plot_width = 300,
		title = "F1 Constructors Nationalities",
		toolbar_location = None,
		tools = "hover",
		tooltips = "@nationality: @n_nat, @percent%",
		x_range = (-1.0, 1.0))
	
	plot_cnats.xaxis.visible = False
	plot_cnats.yaxis.visible = False
	plot_cnats.xgrid.visible = False
	plot_cnats.ygrid.visible = False
	plot_cnats.background_fill_color = 'black'
	#plot.toolbar.autohide = True
	#plot.sizing_mode = "scale_width"
	
	plot_cnats.wedge(x = 0, y = 0,
		radius = 0.9,
		start_angle = cumsum('angle', include_zero = True),
		end_angle = cumsum('angle'),
		line_color = 'black',
		fill_color = 'color',
		#legend_field = 'nationality',
		source = cnats)
	script_cnats, div_cnats = components(plot_cnats)
	
	#cnats = Constructorresults.objects.using('f1').raw('SELECT constructorResultsId,\
		#C.constructorId, points, name, SUM(points) as np FROM constructorResults R\
		#INNER JOIN constructors C ON R.constructorId = C.constructorId\
		#GROUP BY constructorId ORDER BY np DESC')
	#cnats = DataFrame([item.__dict__ for item in cnats])\
		#.drop(columns=['_state', 'constructorresultsid', 'points'])
	
	return render(request, 'f1.html', {'script_dnats': script_dnats,
									   'div_dnats': div_dnats,
		                               'script_cnats': script_cnats,
									   'div_cnats': div_cnats})
