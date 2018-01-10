from django.contrib import admin
from .models import Package, Gallery, GalleryImage

class PackageAdmin(admin.ModelAdmin):

	list_display = ['title', 'travel_date', 'price']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
	
class GalleryAdmin(admin.ModelAdmin):

	list_display = ['title', 'travel_date']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}
	inlines = [GalleryImageInline,]
   
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0

admin.site.register(Package, PackageAdmin)
admin.site.register(Gallery, GalleryAdmin)