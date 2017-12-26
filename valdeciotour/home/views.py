from django.shortcuts import render
from home.models import Package, Gallery
from .forms import ContactValdeciotour

def index(request): 

	packages = Package.objects.all()
	gallery = Gallery.objects.all()
    
	context = {
		'packages': packages,
        'gallery': gallery,
	}
	
	if request.method == 'POST':
		form = ContactValdeciotour(request.POST or None)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactValdeciotour()
	else:
		form = ContactValdeciotour()
	context['form'] = form
	
	return render(request, "home/index.html", context)