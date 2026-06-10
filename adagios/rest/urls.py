from django.urls import re_path
import adagios.rest.views

urlpatterns = [
    re_path(r'^/?$', adagios.rest.views.list_modules),
]

rest_modules = {
    'pynag': 'adagios.misc.helpers',
    'okconfig': 'okconfig',
    'status': 'adagios.rest.status',
    'adagios': 'adagios.misc.rest',
}

for module_name, module_path in list(rest_modules.items()):
    base_pattern = r'^/%s' % module_name
    args = {'module_name': module_name, 'module_path': module_path}
    urlpatterns += [
        re_path(base_pattern + r'/$',   adagios.rest.views.index, args, name="rest/%s" % module_name),
        re_path(base_pattern + r'.js$', adagios.rest.views.javascript, args),
        re_path(base_pattern + r'/(?P<format>.+?)/(?P<attribute>.+?)/?$', adagios.rest.views.handle_request, args),
    ]
