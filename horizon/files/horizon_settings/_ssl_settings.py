
{%- from "horizon/map.jinja" import server with context %}

{%- if server.get('secure', True) %}

USE_SSL = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

{%- endif %}