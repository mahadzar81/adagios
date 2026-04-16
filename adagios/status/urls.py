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
    path('', 'status.views.status_index'),
    path('acknowledgements/', 'status.views.acknowledgement_list'),
    path('error/', 'status.views.error_page'),
    path('comments/', 'status.views.comment_list'),
    path('contacts/', 'status.views.contact_list'),
    path('contactgroups/', 'status.views.contactgroups'),
    path('dashboard/', 'status.views.dashboard'),
    path('detail/', 'status.views.detail'),
    path('downtimes/', 'status.views.downtime_list'),
    path('hostgroups/', 'status.views.status_hostgroups'),
    path('hosts/', 'status.views.hosts'),
    path('log/', 'status.views.log'),
    re_path(r'^map/?$', 'status.views.map_view'),
    path('parents/', 'status.views.network_parents'),
    path('perfdata/', 'status.views.perfdata'),
    path('perfdata2/', 'status.views.perfdata2'),
    path('problems/', 'status.views.problems'),
    path('servicegroups/', 'status.views.status_servicegroups'),
    path('services/', 'status.views.services'),
    path('state_history/', 'status.views.state_history'),
    path('backends/', 'status.views.backends'),



    # Misc snippets
    path('snippets/log/', 'status.views.snippets_log'),
    path('snippets/services/', 'status.views.snippets_services'),
    path('snippets/hosts/', 'status.views.snippets_hosts'),

    # Misc tests
    path('test/services/', 'status.views.services_js'),
    path('test/status_dt/', 'status.views.status_dt'),
    path('test/livestatus/', 'status.views.test_livestatus'),

    # Deprecated as of 2013-03-23
    re_path(r'^contacts/(?P<contact_name>.+)/?$', 'status.views.contact_detail'),
    re_path(r'^hostgroups/(?P<hostgroup_name>.+)/?$', 'status.views.status_hostgroup'),
    re_path(r'^contactgroups/(?P<contactgroup_name>.+)/?$', 'status.views.contactgroup_detail'),
    re_path(r'^servicegroups/(?P<servicegroup_name>.+)/?$', 'status.views.servicegroup_detail'),
    path('services_old/', 'status.views.status'),
]