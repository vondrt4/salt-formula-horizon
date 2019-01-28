{%- from "horizon/map.jinja" import server with context %}
{%- if server.sahara_dashboard.enabled %}

horizon_sahara_packages:
  pkg.installed:
  - names: {{ server.pkgs_sahara }}

{%- endif %}
