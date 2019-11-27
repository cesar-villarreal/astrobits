from django.shortcuts import render
from django.http import HttpResponse

def StuffsView(request):
	text = "BLA"
	return render(request, 'stuff.html', {'content': text, })
