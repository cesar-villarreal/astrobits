from django.shortcuts import render
from .models import Picture, Drivers, Constructors, Driverstandings

import requests

from bs4 import BeautifulSoup

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.transform import cumsum
from bokeh.palettes import viridis 
from bokeh.models import SingleIntervalTicker, HoverTool, ColumnDataSource
from bokeh.layouts import row

from pandas import DataFrame, to_datetime
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

	raw_query = 'SELECT driverId, nationality, COUNT(nationality) AS n_nat\
		FROM drivers GROUP BY nationality ORDER BY n_nat'
	dnats = Drivers.objects.using('f1').raw(raw_query)
	dnats = DataFrame([item.__dict__ for item in dnats])\
		.drop(columns=['_state','driverid'])
	dnats['percent'] = 100*(dnats['n_nat']/dnats['n_nat'].sum())
	dnats['angle'] = dnats['n_nat']/dnats['n_nat'].sum()*2*pi
	dnats['color'] = list(viridis(41))

	plot_dnats = figure(plot_height = 300, plot_width = 300,
		title = "F1 Drivers Nationalities",
		title_location = 'below',
		toolbar_location = None,
		tools = "hover",
		tooltips = "@nationality: @n_nat, @percent%",
		x_range = (-1.0, 1.0))

	plot_dnats.title.align = 'center'
	plot_dnats.xaxis.visible = False
	plot_dnats.yaxis.visible = False
	plot_dnats.xgrid.visible = False
	plot_dnats.ygrid.visible = False
	#plot.toolbar.autohide = True

	plot_dnats.wedge(x = 0, y = 0, radius = 0.9,
		start_angle = cumsum('angle', include_zero = True),
		end_angle = cumsum('angle'),
		line_color = 'black',
		fill_color = 'color',
		#legend_field = 'nationality',
		source = dnats)

	raw_query = 'SELECT constructorId, nationality, COUNT(nationality) AS n_nat\
		FROM constructors GROUP BY nationality ORDER BY n_nat DESC'
	cnats = Constructors.objects.using('f1').raw(raw_query)
	cnats = DataFrame([item.__dict__ for item in cnats]).\
		drop(columns=['_state'])
	cnats['percent'] = 100*(cnats['n_nat']/cnats['n_nat'].sum())
	cnats['angle'] = cnats['n_nat']/cnats['n_nat'].sum()*2*pi
	cnats['color'] = list(viridis(24))

	plot_cnats = figure(plot_height = 300, plot_width = 300,
		title = "F1 Constructors Nationalities",
		title_location = 'below',
		toolbar_location = None,
		tools = "hover",
		tooltips = "@nationality: @n_nat, @percent%",
		x_range = (-1.0, 1.0))

	plot_cnats.title.align = 'center'
	plot_cnats.xaxis.visible = False
	plot_cnats.yaxis.visible = False
	plot_cnats.xgrid.visible = False
	plot_cnats.ygrid.visible = False
	#plot.toolbar.autohide = True

	plot_cnats.wedge(x = 0, y = 0, radius = 0.9,
		start_angle = cumsum('angle', include_zero = True),
		end_angle = cumsum('angle'),
		line_color = 'black',
		fill_color = 'color',
		#legend_field = 'nationality',
		source = cnats)

	#cnats = Constructorresults.objects.using('f1').raw('SELECT constructorResultsId,\
		#C.constructorId, points, name, SUM(points) as np FROM constructorResults R\
		#INNER JOIN constructors C ON R.constructorId = C.constructorId\
		#GROUP BY constructorId ORDER BY np DESC')
	#cnats = DataFrame([item.__dict__ for item in cnats])\
		#.drop(columns=['_state', 'constructorresultsid', 'points'])

	### SERGIO #########################################################################################################
	forename = '"Sergio"' 
	surname = '"Perez"'
	raw_query = 'SELECT driverId FROM drivers\
		WHERE forename = %(forename)s AND surname = %(surname)s'
	driver_id = Drivers.objects.using('f1').raw(raw_query %locals())[0].driverid
	
	raw_query = 'SELECT * FROM driverStandings S INNER JOIN races R\
		ON S.raceId = R.raceId WHERE driverId = %(driver_id)i'
	driver_races = Driverstandings.objects.using('f1').raw(raw_query %locals())
	driver_races = DataFrame([item.__dict__ for item in driver_races]).\
		drop(columns='_state')
	
	cds = ColumnDataSource(driver_races)
	
	plot_points = figure(plot_height = 300, plot_width = 600,
		title = 'Position Vs Time for %(forename)s %(surname)s' %locals(),
		title_location = 'below',
		x_axis_type='datetime',
		toolbar_location = None,)
	plot_points.title.align = "center"
	
	hover = HoverTool(tooltips = [('Date','@date{%Y-%m-%d}'),
		('Position', '@position{int}')], formatters = {'@date': 'datetime'})
	plot_points.add_tools(hover)
	plot_points.y_range.flipped = True
	plot_points.xaxis.major_label_orientation = 45
	plot_points.xaxis[0].ticker.desired_num_ticks =\
		int((driver_races['date'].max() - driver_races['date'].min()).\
		days/365.25)
	
	plot_points.scatter('date', 'position', source=cds)
	
	script_nats , div_nats = components(row(plot_cnats, plot_dnats), theme = 'dark_minimal')
	script_points, div_points = components(plot_points, theme = 'dark_minimal')
	
	return render(request, 'f1.html', {'script_nats': script_nats,
									   'div_nats': div_nats,
									   'script_points': script_points,
									   'div_points': div_points})
