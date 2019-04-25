{%- from "horizon/map.jinja" import server with context %}

{%- if server.app is defined %}
{%- set app = server.app.app_name %}
{%- else %}
{%- set app = server %}
{%- endif %}

{% if app.openstack_heat_stack is defined %}
OPENSTACK_HEAT_STACK = {
{%- for key, value in app.openstack_heat_stack.iteritems() %}
    "{{ key }}": {{ value }}{% if not loop.last %},{% endif %}
{%- endfor %}
}
{%- endif %}
