from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'index-jq/', views.indexjq, name='index jq'),
	url(r'money/', views.money, name='money'),
    url(r'', views.index, name='index'),
]