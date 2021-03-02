from django.shortcuts import render
from .models import Picture, Drivers, Constructors, Driverstandings
import requests
from bs4 import BeautifulSoup
from .functions.f1Dash import dnats, cnats, driver_position, dropdown_drivers
from bokeh.embed import components
from bokeh.layouts import row, column
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

	from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select
	from bokeh.plotting import figure
	from pandas import DataFrame

#######################################################################################################################
	raw_query = 'SELECT driverStandingsId, S.raceId, position, driverId, R.date\
	             FROM driverStandings S INNER JOIN races R ON S.raceId = R.raceId'
	driver_races = Driverstandings.objects.using('f1').raw(raw_query %locals())
	driver_races = DataFrame([item.__dict__ for item in driver_races]).\
                   drop(columns='_state')

	cds0 = ColumnDataSource(driver_races)
	cds1 = ColumnDataSource(driver_races)
	
	plot = figure(plot_height = 300, plot_width = 600,
		title = 'Position Vs Time',
		title_location = 'below',
		x_axis_type='datetime',
		tools="pan,wheel_zoom,box_zoom,reset",
		toolbar_location = 'right',
		x_axis_label='Year',
		y_axis_label='Position')
	hover = HoverTool(tooltips = [('Date','@date{%Y-%m-%d}'),
								  ('Position', '@position{int}')],
                                  formatters = {'@date': 'datetime'})
	plot.add_tools(hover)
	plot.sizing_mode = 'scale_width'
	plot.title.align = "center"
	plot.y_range.flipped = True
	plot.xaxis.major_label_orientation = 45
	plot.xaxis[0].ticker.desired_num_ticks =\
		int((driver_races['date'].max() - driver_races['date'].min()).\
		days/365.25)
	plot.scatter('date', 'position', source=cds0)
	callback = CustomJS(args = dict(cds0 = cds0, cds1 = cds1), code = """
						var dropdown_value = cb_obj.value;

						var data0 = cds0.data;
						var data1 = cds1.data;

						data0['date'] = []
						data0['position'] = []

						for (var i = 0; i < 32000; i++){
							if ( data1['driverid'][i] == 815 ){
								data0['date'].push(data1['date'][i])
								data0['position'].push(data1['position'][i])
							}
						}
						
						cds0.change.emit();
                    
                     """)
	dropdown = Select(title ='Test', options = ['0','1','2'])
	dropdown.js_on_change('value', callback)
	script, div = components(column(plot, dropdown), theme='dark_minimal')
########################################################################################################################






	plot_dnats = dnats(Drivers)
	plot_cnats = cnats(Constructors)
	plot_driver_position = driver_position(Drivers, Driverstandings)
	drop_drivers = dropdown_drivers(Drivers)
	
	script_nats, div_nats = components(row(plot_dnats, plot_cnats),
                                       theme = 'dark_minimal')
	script_position, div_position = components(column(plot_driver_position, drop_drivers), theme = 'dark_minimal')

	return render(request, 'f1.html', {'script_nats': script_nats,
									   'div_nats': div_nats,
									   'script_position': script_position,
									   'div_position': div_position,
									   'script': script,
									   'div': div
									   })
