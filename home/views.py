from django.shortcuts import render

def indexView(request):
	title = "Home"
	return render(request, 'home.html', {'title': title })

def aboutView(request):
	title = "About"
	return render(request, 'about.html', {'title': title })