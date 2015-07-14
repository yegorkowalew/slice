from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'index-jq/', views.indexjq, name='index jq'),
	url(r'acceslog-jq/', views.acceslogjq, name='acceslog jq'),
	url(r'shortcuts-jq/', views.shortcutsjq, name='shortcuts jq'),
	url(r'money/', views.money, name='money'),
    url(r'', views.index, name='index'),
]