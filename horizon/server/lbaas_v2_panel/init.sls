{%- from "horizon/map.jinja" import server with context %}
{%- if server.lbaas_v2_panel.enabled %}

horizon_octavia_packages:
  pkg.installed:
  - names: {{ server.pkgs_octavia }}

{%- endif %}
