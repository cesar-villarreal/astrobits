from django.shortcuts import render

def indexView(request):
	text = "BLA"
	return render(request, 'stuff.html', {'content': text, })