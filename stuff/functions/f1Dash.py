from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.palettes import viridis 
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select
from pandas import DataFrame, to_datetime
from math import pi



def dnats(Drivers):
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

	plot_dnats.sizing_mode = 'scale_both'
	plot_dnats.title.align = 'center'
	plot_dnats.xaxis.visible = False
	plot_dnats.yaxis.visible = False
	plot_dnats.xgrid.visible = False
	plot_dnats.ygrid.visible = False
	plot_dnats.toolbar.autohide = True

	plot_dnats.wedge(x = 0, y = 0, radius = 0.9,
		start_angle = cumsum('angle', include_zero = True),
		end_angle = cumsum('angle'),
		line_color = 'black',
		fill_color = 'color',
		#legend_field = 'nationality',
		source = dnats)
	
	return plot_dnats

def cnats(Constructors):
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

	plot_cnats.sizing_mode = 'scale_both'
	plot_cnats.title.align = 'center'
	plot_cnats.xaxis.visible = False
	plot_cnats.yaxis.visible = False
	plot_cnats.xgrid.visible = False
	plot_cnats.ygrid.visible = False
	plot_cnats.toolbar.autohide = True

	plot_cnats.wedge(x = 0, y = 0, radius = 0.9,
		start_angle = cumsum('angle', include_zero = True),
		end_angle = cumsum('angle'),
		line_color = 'black',
		fill_color = 'color',
		#legend_field = 'nationality',
		source = cnats)
	
	return plot_cnats

def driver_position(Drivers, Driverstandings):
	forename = '"Sergio"'
	surname = '"Perez"'
	
	raw_query = 'SELECT driverId FROM drivers\
		WHERE forename = %(forename)s AND surname = %(surname)s'
	driver_id = Drivers.objects.using('f1').raw(raw_query %locals())[0].driverid
	
	raw_query = 'SELECT * FROM driverStandings S INNER JOIN races R\
		ON S.raceId = R.raceId WHERE driverId = 815'
	driver_races = Driverstandings.objects.using('f1').raw(raw_query %locals())
	driver_races = DataFrame([item.__dict__ for item in driver_races]).\
		drop(columns='_state')
	
	cds = ColumnDataSource(driver_races)
	
	plot_driver = figure(plot_height = 300, plot_width = 600,
		title = 'Position Vs Time for %(forename)s %(surname)s' %locals(),
		title_location = 'below',
		x_axis_type='datetime',
		tools="pan,wheel_zoom,box_zoom,reset",
		toolbar_location = 'right',
		x_axis_label='Year',
		y_axis_label='Position')
	
	hover = HoverTool(tooltips = [('Date','@date{%Y-%m-%d}'),
								  ('Position', '@position{int}')],
                                  formatters = {'@date': 'datetime'})
	
	plot_driver.add_tools(hover)
	plot_driver.sizing_mode = 'scale_width'
	plot_driver.title.align = "center"
	plot_driver.y_range.flipped = True
	plot_driver.xaxis.major_label_orientation = 45
	plot_driver.xaxis[0].ticker.desired_num_ticks =\
		int((driver_races['date'].max() - driver_races['date'].min()).\
		days/365.25)
	
	plot_driver.scatter('date', 'position', source=cds)
	
	return plot_driver

def dropdown_drivers(Drivers):
	raw_query = 'SELECT driverId, forename, surname FROM drivers ORDER BY forename'
	drivers_names = Drivers.objects.using('f1').raw(raw_query)
	drivers_names = DataFrame([item.__dict__ for item in drivers_names]).\
				   drop(columns='_state')
	drivers_names['name'] = drivers_names['forename'] + ' ' + drivers_names['surname']
	
	return Select(title="Driver",
                  options=drivers_names['name'].to_list(),
                  width = 200)

#cnats = Constructorresults.objects.using('f1').raw('SELECT constructorResultsId,\
	#C.constructorId, points, name, SUM(points) as np FROM constructorResults R\
	#INNER JOIN constructors C ON R.constructorId = C.constructorId\
	#GROUP BY constructorId ORDER BY np DESC')
#cnats = DataFrame([item.__dict__ for item in cnats])\
	#.drop(columns=['_state', 'constructorresultsid', 'points'])
