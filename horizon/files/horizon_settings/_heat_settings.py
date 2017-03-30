{%- from "horizon/map.jinja" import server with context %}

{%- if server.app is defined %}
{%- set app = server.app.app_name %}
{%- else %}
{%- set app = server %}
{%- endif %}

{%- if app.get('openstack_heat_stack', false) %}
OPENSTACK_HEAT_STACK = {'enable_user_pass': True}
{%- endif %}
