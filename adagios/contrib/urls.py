from django.urls import re_path
import adagios.contrib.views

urlpatterns = [
    re_path(r'^/$', adagios.contrib.views.index),
    re_path(r'^/(?P<arg1>.+)?$', adagios.contrib.views.contrib),
    re_path(r'^/(?P<arg1>.+)/(?P<arg2>.+)/?$', adagios.contrib.views.contrib),
    re_path(r'^/(?P<arg1>.+)(?P<arg2>.+)/(?P<arg3>.+)/?$', adagios.contrib.views.contrib),
    re_path(r'^/(?P<arg1>.+)(?P<arg2>.+)/(?P<arg3>.+)/(?P<arg4>.+)/?$', adagios.contrib.views.contrib),
]
