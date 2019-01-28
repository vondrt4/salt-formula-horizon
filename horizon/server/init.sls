include:
{%- if pillar.horizon.server.app is defined %}
{# uglier way, for development #}
- horizon.server.multi.service
- horizon.server.multi.site
{%- else %}
{# production way #}
- horizon.server.service
{%- if pillar.horizon.server.plugin is defined %}
- horizon.server.plugin
{%- endif %}
{%- if pillar.horizon.server.ssl is defined %}
- horizon.server.ssl
{%- endif %}
{%- if pillar.horizon.server.sahara_dashboard is defined %}
- horizon.server.sahara_dashboard
{%- endif %}
{%- if pillar.horizon.server.manila_ui is defined %}
- horizon.server.manila_ui
{%- endif %}
{%- endif %}
