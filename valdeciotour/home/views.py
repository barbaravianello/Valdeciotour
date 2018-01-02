from django.shortcuts import render
from home.models import Package, Gallery
from .forms import ContactValdeciotour, LeadForm
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request): 

	packages = Package.objects.all()
	gallery = Gallery.objects.all()
	
	context = {
		'packages': packages,
        'gallery': gallery,
	}
	
	if request.method == 'POST':
		form = ContactValdeciotour(request.POST or None)
		subform = LeadForm(request.POST or None)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactValdeciotour()
		if subform.is_valid():
			context['is_valid'] = True
			subform.save_contact()
			subform = LeadForm()
	else:
		form = ContactValdeciotour()
		subform = LeadForm()
	context['form'] = form
	context['subform'] = subform
	
	return render(request, "home/index.html", context)
