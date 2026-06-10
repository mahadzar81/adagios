from django.urls import re_path
import adagios.status.views

urlpatterns = [
    re_path(r'^/?$', adagios.status.views.status_index),
    re_path(r'^/acknowledgements/?$', adagios.status.views.acknowledgement_list),
    re_path(r'^/error/?$', adagios.status.views.error_page),
    re_path(r'^/comments/?$', adagios.status.views.comment_list),
    re_path(r'^/contacts/?$', adagios.status.views.contact_list),
    re_path(r'^/contactgroups/?$', adagios.status.views.contactgroups),
    re_path(r'^/dashboard/?$', adagios.status.views.dashboard),
    re_path(r'^/detail/?$', adagios.status.views.detail),
    re_path(r'^/downtimes/?$', adagios.status.views.downtime_list),
    re_path(r'^/hostgroups/?$', adagios.status.views.status_hostgroups),
    re_path(r'^/hosts/?$', adagios.status.views.hosts),
    re_path(r'^/log/?$', adagios.status.views.log),
    re_path(r'^/map/?', adagios.status.views.map_view),
    re_path(r'^/parents/?$', adagios.status.views.network_parents),
    re_path(r'^/perfdata/?$', adagios.status.views.perfdata),
    re_path(r'^/perfdata2/?$', adagios.status.views.perfdata2),
    re_path(r'^/problems/?$', adagios.status.views.problems),
    re_path(r'^/servicegroups/?$', adagios.status.views.status_servicegroups),
    re_path(r'^/services/?$', adagios.status.views.services),
    re_path(r'^/state_history/?$', adagios.status.views.state_history),
    re_path(r'^/backends/?$', adagios.status.views.backends),
    # Snippets
    re_path(r'^/snippets/log/?$', adagios.status.views.snippets_log),
    re_path(r'^/snippets/services/?$', adagios.status.views.snippets_services),
    re_path(r'^/snippets/hosts/?$', adagios.status.views.snippets_hosts),
    # Tests
    re_path(r'^/test/services/?$', adagios.status.views.services_js),
    re_path(r'^/test/status_dt/?$', adagios.status.views.status_dt),
    re_path(r'^/test/livestatus/?$', adagios.status.views.test_livestatus),
    # Deprecated
    re_path(r'^/contacts/(?P<contact_name>.+)/?$', adagios.status.views.contact_detail),
    re_path(r'^/hostgroups/(?P<hostgroup_name>.+)/?$', adagios.status.views.status_hostgroup),
    re_path(r'^/contactgroups/(?P<contactgroup_name>.+)/?$', adagios.status.views.contactgroup_detail),
    re_path(r'^/servicegroups/(?P<servicegroup_name>.+)/?$', adagios.status.views.servicegroup_detail),
    re_path(r'^/services_old/?$', adagios.status.views.status),
]
