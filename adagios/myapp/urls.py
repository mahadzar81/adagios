from django.urls import re_path
import adagios.myapp.views

urlpatterns = [
    re_path(r'^/?$', adagios.myapp.views.hello_world),
    re_path(r'^/url1?$', adagios.myapp.views.hello_world),
    re_path(r'^/url2?$', adagios.myapp.views.hello_world),
]
