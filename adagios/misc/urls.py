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

from django.urls import path, re_path

urlpatterns = [
    re_path(r'^test/?$', 'adagios.misc.views.test'),
    re_path(r'^paste/?$', 'adagios.misc.views.paste'),
    path('', 'adagios.misc.views.index'),

    re_path(r'^settings/?$', 'adagios.misc.views.settings'),
    re_path(r'^preferences/?$', 'adagios.misc.views.preferences'),
    re_path(r'^nagios/?$', 'adagios.misc.views.nagios'),
    re_path(r'^iframe/?$', 'adagios.misc.views.iframe'),
    re_path(r'^gitlog/?$', 'adagios.misc.views.gitlog'),
    re_path(r'^service/?$', 'adagios.misc.views.nagios_service'),
    path('pnp4nagios/', 'adagios.misc.views.pnp4nagios'),
    re_path(r'^pnp4nagios/edit(?P<filename>.+)$', 'adagios.misc.views.pnp4nagios_edit_template'),
    re_path(r'^mail$', 'adagios.misc.views.mail'),
    re_path(r'^images/(?P<path>.+)$', 'django.views.static.serve', {'document_root': '/usr/share/nagios3/htdocs/images/logos/'}, name="logo"),
    path('images/', 'adagios.misc.views.icons'),
]