from django.urls import re_path
from django.views.static import serve
import adagios.misc.views

urlpatterns = [
    re_path(r'^/test/?', adagios.misc.views.test),
    re_path(r'^/paste/?', adagios.misc.views.paste),
    re_path(r'^/?$', adagios.misc.views.index),
    re_path(r'^/settings/?', adagios.misc.views.settings),
    re_path(r'^/preferences/?', adagios.misc.views.preferences),
    re_path(r'^/nagios/?', adagios.misc.views.nagios),
    re_path(r'^/iframe/?', adagios.misc.views.iframe),
    re_path(r'^/gitlog/?', adagios.misc.views.gitlog),
    re_path(r'^/service/?', adagios.misc.views.nagios_service),
    re_path(r'^/pnp4nagios/?$', adagios.misc.views.pnp4nagios),
    re_path(r'^/pnp4nagios/edit(?P<filename>.+)$', adagios.misc.views.pnp4nagios_edit_template),
    re_path(r'^/mail', adagios.misc.views.mail),
    re_path(r'^/images/(?P<path>.+)$', serve, {'document_root': '/usr/share/nagios3/htdocs/images/logos/'}, name="logo"),
    re_path(r'^/images/?$', adagios.misc.views.icons),
]
