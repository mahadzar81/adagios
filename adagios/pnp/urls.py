from django.urls import re_path
import adagios.pnp.views

urlpatterns = [
    re_path(r'^/(?P<pnp_command>.+)?$', adagios.pnp.views.pnp),
]
