from django.urls import re_path
import adagios.bi.views

urlpatterns = [
    re_path(r'^/?$', adagios.bi.views.index),
    re_path(r'^/add/?$', adagios.bi.views.add),
    re_path(r'^/add/subprocess/?$', adagios.bi.views.add_subprocess),
    re_path(r'^/add/graph/?$', adagios.bi.views.add_graph),
    re_path(r'^/(?P<process_name>.+)/edit/status_method$', adagios.bi.views.change_status_calculation_method),
    re_path(r'^/edit/(?P<process_type>.+?)/(?P<process_name>.+?)/?$', adagios.bi.views.edit),
    re_path(r'^/json/(?P<process_type>.+?)/(?P<process_name>.+?)/?$', adagios.bi.views.json),
    re_path(r'^/graphs/(?P<process_type>.+?)/(?P<process_name>.+?)/?$', adagios.bi.views.graphs_json),
    re_path(r'^/delete/(?P<process_type>.+?)/(?P<process_name>.+?)/?$', adagios.bi.views.delete),
    re_path(r'^/view/(?P<process_type>.+?)/(?P<process_name>.+?)/?$', adagios.bi.views.view),
]
