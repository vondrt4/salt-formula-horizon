{%- from "horizon/map.jinja" import server with context %}
{%- if server.manila_ui.enabled %}

horizon_manila_packages:
  pkg.installed:
  - names: {{ server.pkgs_manila }}

{%- endif %}
