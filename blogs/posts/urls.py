from django.conf.urls import url
from django.contrib import admin
from .views import (
	blogviewlist,
	blogviewcreate,
	blogviewread,
	blogviewupdate,
	blogviewdelete,
	blogviewmake,
	)

urlpatterns = [
    url(r'^list/$',blogviewlist,name='list'),
    url(r'^create/$',blogviewcreate,name='create'),
    url(r'^(?P<id>\d+)/$',blogviewread,name='detail'),
	url(r'^(?P<id>\d+)/update$',blogviewupdate,name='update'),
    url(r'^(?P<id>\d+)/delete/$',blogviewdelete),
    url(r'^make/$',blogviewmake),

      
]