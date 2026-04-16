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

from django.urls import path, include, re_path
from adagios import settings
from django.views.static import serve
from django.views.i18n import JavaScriptCatalog
from adagios import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Example:
    path('', views.index, name="home"),
    path('403', views.http_403),
    path('objectbrowser/', include('adagios.objectbrowser.urls')),
    path('status/', include('adagios.status.urls')),
    path('bi/', include('adagios.bi.urls')),
    path('misc/', include('adagios.misc.urls')),
    path('pnp/', include('adagios.pnp.urls')),
    re_path(r'^media(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('rest/', include('adagios.rest.urls')),
    path('contrib/', include('adagios.contrib.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    # Internationalization
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name="media"),
    ]
        

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()

