from django.urls import re_path
import adagios.okconfig_.views

urlpatterns = [
    re_path(r'^/scan_network/?', adagios.okconfig_.views.scan_network),
    re_path(r'^/addgroup/?', adagios.okconfig_.views.addgroup),
    re_path(r'^/addtemplate/?', adagios.okconfig_.views.addtemplate),
    re_path(r'^/addhost/?', adagios.okconfig_.views.addhost),
    re_path(r'^/addservice/?', adagios.okconfig_.views.addservice),
    re_path(r'^/install_agent/?', adagios.okconfig_.views.install_agent),
    re_path(r'^/edit/?$', adagios.okconfig_.views.choose_host),
    re_path(r'^/edit/(?P<host_name>.+)$', adagios.okconfig_.views.edit),
    re_path(r'^/verify_okconfig/?', adagios.okconfig_.views.verify_okconfig),
]
