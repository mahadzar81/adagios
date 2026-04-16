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
from objectbrowser import views


urlpatterns = [

    path('', views.list_object_types, name="objectbrowser"),

    re_path(r'^/edit_all/(?P<object_type>.+)/(?P<attribute_name>.+)/?$', views.edit_all),
    path('search/', views.search_objects, name="search"),


    re_path(r'^/edit/(?P<object_id>.+?)?$', views.edit_object, name="edit_object"),
    path('import/', views.import_objects),
    path('edit/', views.edit_object),
    re_path(r'^/copy_and_edit/(?P<object_id>.+?)?$', views.copy_and_edit_object),

    re_path(r'^/copy/(?P<object_id>.+)$', views.copy_object, name="copy_object"),
    re_path(r'^/delete/(?P<object_id>.+)$', views.delete_object, name="delete_object"),
    re_path(r'^/delete/(?P<object_type>.+?)/(?P<shortname>.+)/?$', views.delete_object_by_shortname, name="delete_by_shortname"),

    re_path(r'^/add/(?P<object_type>.+)$', views.add_object, name="addobject"),
    path('bulk_edit/', views.bulk_edit, name='bulk_edit'),
    path('bulk_delete/', views.bulk_delete, name='bulk_delete'),
    path('bulk_copy/', views.bulk_copy, name='bulk_copy'),
    re_path(r'^/add_to_group/(?P<group_type>.+)/(?P<group_name>.+)/?$', views.add_to_group),
    re_path(r'^/add_to_group/(?P<group_type>.+)/?$', views.add_to_group),
    path('add_to_group', views.add_to_group),
    path('plugins/', views.show_plugins),
    path('nagios.cfg/', views.edit_nagios_cfg),
    path('nagios.cfg/edit/', views.edit_nagios_cfg),
    re_path(r'^/geek_edit/id=(?P<object_id>.+)$', views.geek_edit),
    re_path(r'^/advanced_edit/id=(?P<object_id>.+)$', views.advanced_edit),

    # Here for backwards compatibility.
    re_path(r'^/edit/id=(?P<object_id>.+)$', views.edit_object),
    re_path(r'^/id=(?P<object_id>.+)$', views.edit_object),

    # These should be deprecated as of 2012-08-27
    re_path(r'^/copy_object/id=(?P<object_id>.+)$', views.copy_object),
    re_path(r'^/delete_object/id=(?P<object_id>.+)$', views.delete_object),

]
