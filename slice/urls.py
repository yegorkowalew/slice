"""slice URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'', include('money.urls')),
	# url(r'^index/', include('money.urls')),
	url(r'^admin/', include(admin.site.urls)),
]
