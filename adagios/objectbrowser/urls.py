from django.urls import re_path
import adagios.objectbrowser.views
import adagios.misc.views

urlpatterns = [
    re_path(r'^/$', adagios.objectbrowser.views.list_object_types, name="objectbrowser"),
    re_path(r'^/edit_all/(?P<object_type>.+)/(?P<attribute_name>.+)/?$', adagios.objectbrowser.views.edit_all),
    re_path(r'^/search/?$', adagios.objectbrowser.views.search_objects, name="search"),
    re_path(r'^/edit/(?P<object_id>.+?)?$', adagios.objectbrowser.views.edit_object, name="edit_object"),
    re_path(r'^/import/?$', adagios.objectbrowser.views.import_objects),
    re_path(r'^/edit/?$', adagios.objectbrowser.views.edit_object),
    re_path(r'^/copy_and_edit/(?P<object_id>.+?)?$', adagios.objectbrowser.views.copy_and_edit_object),
    re_path(r'^/copy/(?P<object_id>.+)$', adagios.objectbrowser.views.copy_object, name="copy_object"),
    re_path(r'^/delete/(?P<object_id>.+)$', adagios.objectbrowser.views.delete_object, name="delete_object"),
    re_path(r'^/delete/(?P<object_type>.+?)/(?P<shortname>.+)/?$', adagios.objectbrowser.views.delete_object_by_shortname, name="delete_by_shortname"),
    re_path(r'^/add/(?P<object_type>.+)$', adagios.objectbrowser.views.add_object, name="addobject"),
    re_path(r'^/bulk_edit/?$', adagios.objectbrowser.views.bulk_edit, name='bulk_edit'),
    re_path(r'^/bulk_delete/?$', adagios.objectbrowser.views.bulk_delete, name='bulk_delete'),
    re_path(r'^/bulk_copy/?$', adagios.objectbrowser.views.bulk_copy, name='bulk_copy'),
    re_path(r'^/add_to_group/(?P<group_type>.+)/(?P<group_name>.+)/?$', adagios.objectbrowser.views.add_to_group),
    re_path(r'^/add_to_group/(?P<group_type>.+)/?$', adagios.objectbrowser.views.add_to_group),
    re_path(r'^/add_to_group', adagios.objectbrowser.views.add_to_group),
    re_path(r'^/plugins/?$', adagios.objectbrowser.views.show_plugins),
    re_path(r'^/nagios.cfg/?$', adagios.objectbrowser.views.edit_nagios_cfg),
    re_path(r'^/nagios.cfg/edit/?$', adagios.misc.views.edit_nagios_cfg),
    re_path(r'^/geek_edit/id=(?P<object_id>.+)$', adagios.objectbrowser.views.geek_edit),
    re_path(r'^/advanced_edit/id=(?P<object_id>.+)$', adagios.objectbrowser.views.advanced_edit),
    # Backwards compatibility
    re_path(r'^/edit/id=(?P<object_id>.+)$', adagios.objectbrowser.views.edit_object),
    re_path(r'^/id=(?P<object_id>.+)$', adagios.objectbrowser.views.edit_object),
    # Deprecated
    re_path(r'^/copy_object/id=(?P<object_id>.+)$', adagios.objectbrowser.views.copy_object),
    re_path(r'^/delete_object/id=(?P<object_id>.+)$', adagios.objectbrowser.views.delete_object),
]
