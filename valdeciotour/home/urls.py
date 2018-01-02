from home import views
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)