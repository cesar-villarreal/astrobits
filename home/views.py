from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SendMail

def indexView(request):
	title = "Home"
	return render(request, 'home.html', {'title': title })

def aboutView(request):
	title = "About"
	return render(request, 'about.html', {'title': title })

def ContactView(request):
	title = "Contact"

	if request.method == "POST":
		send_mail(request.POST.get('subject'),
                  request.POST.get('message'),
                  "astro@cvillarreal.xyz",
                  [request.POST.get("contact_mail"), "astro@cvillarreal.xyz"])	

		return render(request, 'contact.html', {'title': title,
                                                'SendMail': SendMail,
                                                'email_success': 'Your E-mail has been sent!'})
	if request.method == "GET":
		return render(request, 'contact.html', {'title': title,
                                                'SendMail': SendMail})
