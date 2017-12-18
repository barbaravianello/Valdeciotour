from django.shortcuts import render
from home.models import Package

def index(request): 

	packages = Package.objects.all()

	context = {
		'packages': packages,	
	}
	return render(request, "home/index.html", context)