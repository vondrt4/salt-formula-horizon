import os
from django.utils.translation import ugettext_lazy as _
from openstack_dashboard import exceptions

{%- from "horizon/map.jinja" import server with context %}

{%- if server.app is defined %}
{%- set app = salt['pillar.get']('horizon:server:app:'+app_name) %}
{%- else %}
{%- set app = salt['pillar.get']('horizon:server') %}
{%- endif %}

{% include "horizon/files/horizon_settings/_horizon_config.py" %}


{%- if app.theme is defined or (app.plugin is defined and app.plugin.horizon_theme is defined) %}
{%- if app.theme is defined %}
CUSTOM_THEME_PATH = 'themes/{{ app.theme }}'
{%- elif app.plugin.horizon_theme.theme_name is defined %}
# Enable custom theme if it is present.
try:
  from openstack_dashboard.enabled._99_horizon_theme import CUSTOM_THEME_PATH
except ImportError:
  pass
{%- endif %}
{%- endif %}

INSTALLED_APPS = (
    'openstack_dashboard',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'compressor',
    'horizon',
    'openstack_auth',
    {%- if app.logging is defined %}
    'raven.contrib.django.raven_compat',
    {%- endif %}
)

{% include "horizon/files/horizon_settings/_local_settings.py" %}
{% include "horizon/files/horizon_settings/_horizon_settings.py" %}
{% include "horizon/files/horizon_settings/_keystone_settings.py" %}
{% include "horizon/files/horizon_settings/_nova_settings.py" %}
{% include "horizon/files/horizon_settings/_glance_settings.py" %}
{% include "horizon/files/horizon_settings/_neutron_settings.py" %}
{% include "horizon/files/horizon_settings/_websso_settings.py" %}
