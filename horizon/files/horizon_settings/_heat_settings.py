{%- from "horizon/map.jinja" import server with context %}

{%- if server.app is defined %}
{%- set app = server.app.app_name %}
{%- else %}
{%- set app = server %}
{%- endif %}

{% if app.openstack_heat_stack is defined %}
OPENSTACK_HEAT_STACK = {'enable_user_pass': {% if app.openstack_heat_stack %}True{% else %}False{% endif %}}
{%- endif %}
