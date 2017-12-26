from django.contrib import admin
from .models import Package, Gallery

class PackageAdmin(admin.ModelAdmin):

	list_display = ['title', 'travel_date', 'price']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

    
class GalleryAdmin(admin.ModelAdmin):

	list_display = ['title', 'travel_date']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Package, PackageAdmin)
admin.site.register(Gallery, GalleryAdmin)