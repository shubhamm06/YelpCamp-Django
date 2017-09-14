from django.conf.urls import url
from . import views

# urls

app_name = 'campgrounds'

urlpatterns = [
	url(r'^$', views.CampgroundList.as_view(), name='all'),
	url(r'^new/$', views.CreateCampground.as_view(), name='create'),
]