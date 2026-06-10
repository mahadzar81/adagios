# Adagios is a web based Nagios configuration interface
#
# Copyright (C) 2014, Pall Sigurdsson <palli@opensource.is>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.urls import re_path, include
from adagios import settings
from django.views.static import serve
import adagios.views
import django.views.i18n

urlpatterns = [
    re_path(r'^$', adagios.views.index, name="home"),
    re_path(r'^403', adagios.views.http_403),
    re_path(r'^objectbrowser', include('adagios.objectbrowser.urls')),
    re_path(r'^status', include('adagios.status.urls')),
    re_path(r'^bi', include('adagios.bi.urls')),
    re_path(r'^misc', include('adagios.misc.urls')),
    re_path(r'^pnp', include('adagios.pnp.urls')),
    re_path(r'^media(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^rest', include('adagios.rest.urls')),
    re_path(r'^contrib', include('adagios.contrib.urls')),
    # Internationalization
    re_path(r'^jsi18n/$', django.views.i18n.JavaScriptCatalog.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name="media"),
    ]
