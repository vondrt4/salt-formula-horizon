
===============
Horizon Formula
===============

Horizon is the canonical implementation of OpenStack’s Dashboard, which
provides a web based user interface to OpenStack services including Nova,
Swift, Keystone, etc.


Sample Pillars
==============

Simplest horizon setup

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        secret_key: secret
        host:
          name: cloud.lab.cz
        cache:
          engine: 'memcached'
          host: '127.0.0.1'
          port: 11211
          prefix: 'CACHE_HORIZON'
        api_versions:
          identity: 2
        identity:
          engine: 'keystone'
          host: '127.0.0.1'
          port: 5000
        mail:
          host: '127.0.0.1'

Simple branded horizon

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        branding: 'OpenStack Company Dashboard'
        default_dashboard: 'admin'
        help_url: 'http://doc.domain.com'

Horizon with policy files metadata. With source mine you can obtain real time policy file state from targeted node (OpenStack control node), provided you have policy file published to specified grain key. Source file will obtain static policy definition from formula files directory.

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        policy:
          identity:
            source: mine
            host: ctl01.my-domain.local
            name: keystone_policy.json
            grain_name: keystone_policy
            enabled: true
          compute:
            source: file
            name: nova_policy.json
            enabled: true
          network:
            source: file
            name: neutron_policy.json
            enabled: true
          image:
            source: file
            name: glance_policy.json
            enabled: true
          volume:
            source: file
            name: cinder_policy.json
            enabled: true
          telemetry:
            source: file
            name: ceilometer_policy.json
            enabled: true
          orchestration:
            source: file
            name: heat_policy.json
            enabled: true

Horizon with enabled SSL security (when SSL is realised by proxy)

.. code-block:: yaml

    horizon:
      server:
        enabled: True
        secure: True


Horizon package setup with SSL

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        secret_key: MEGASECRET
        version: juno
        ssl:
          enabled: true
          authority: CA_Authority
        host:
          name: cloud.lab.cz
        cache:
          engine: 'memcached'
          host: '127.0.0.1'
          port: 11211
          prefix: 'CACHE_HORIZON'
        api_versions:
          identity: 2
        identity:
          engine: 'keystone'
          host: '127.0.0.1'
          port: 5000
        mail:
          host: '127.0.0.1'

Horizon with custom SESSION_ENGINE (default is "signed_cookies", valid options are: "signed_cookies", "cache", "file") and SESSION_TIMEOUT

.. code-block:: yaml

    horizon:
      server:
        enabled: True
        secure: True
        session:
          engine: 'cache'
          timeout: 43200

Multi-regional horizon setup

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: juno
        secret_key: MEGASECRET
        cache:
          engine: 'memcached'
          host: '127.0.0.1'
          port: 11211
          prefix: 'CACHE_HORIZON'
        api_versions:
          identity: 2
        identity:
          engine: 'keystone'
          host: '127.0.0.1'
          port: 5000
        mail:
          host: '127.0.0.1'
        regions:
        - name: cluster1
          address: http://cluster1.example.com:5000/v2.0
        - name: cluster2
          address: http://cluster2.example.com:5000/v2.0

Horizon setup with sensu plugin

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: juno
        sensu_api:
          host: localhost
          port: 4567
        plugin:
          monitoring:
            app: horizon_monitoring
            source:
              type: git
              address: git@repo1.robotice.cz:django/horizon-monitoring.git
              rev: develop

Sensu multi API

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: juno
        sensu_api:
          dc1:
            host: localhost
            port: 4567
          dc2:
            host: anotherhost
            port: 4567

Horizon setup with jenkins plugin

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: juno
        jenkins_api:
          url: https://localhost:8080
          user: admin
          password: pwd
        plugin:
          jenkins:
            app: horizon_jenkins
            source:
              type: pkg

Horizon setup with billometer plugin

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: juno
        billometer_api:
          host: localhost
          port: 9753
          api_version: 1
        plugin:
          billing:
            app: horizon_billing
            source:
              type: git
              address: git@repo1.robotice.cz:django/horizon-billing.git
              rev: develop

Horizon setup with contrail plugin

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: icehouse
        plugin:
          contrail:
            app: contrail_openstack_dashboard
            override: true
            source:
              type: git
              address: git@repo1.robotice.cz:django/horizon-contrail.git
              rev: develop

Horizon setup with sentry log handler

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        version: juno
        ...
        logging:
          engine: raven
          dsn: http://pub:private@sentry1.test.cz/2

Multisite with Git source
-------------------------

Simple Horizon setup from git repository

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        app:
          default:
            secret_key: MEGASECRET
            source:
              engine: git
              address: https://github.com/openstack/horizon.git
              rev: stable/havana
            cache:
              engine: 'memcached'
              host: '127.0.0.1'
              port: 11211
              prefix: 'CACHE_DEFAULT'
            api_versions:
              identity: 2
            identity:
              engine: 'keystone'
              host: '127.0.0.1'
              port: 5000
            mail:
              host: '127.0.0.1'

Themed multisite setup

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        app:
          openstack1c:
            secret_key: MEGASECRET1
            source:
              engine: git
              address: https://github.com/openstack/horizon.git
              rev: stable/havana
            plugin:
              contrail:
                app: contrail_openstack_dashboard
                override: true
                source:
                  type: git
                  address: git@repo1.robotice.cz:django/horizon-contrail.git
                  rev: develop
              theme:
                app: site1_theme
                source:
                  type: git
                  address: git@repo1.domain.com:django/horizon-site1-theme.git
            cache:
              engine: 'memcached'
              host: '127.0.0.1'
              port: 11211
              prefix: 'CACHE_SITE1'
            api_versions:
              identity: 2
            identity:
              engine: 'keystone'
              host: '127.0.0.1'
              port: 5000
            mail:
              host: '127.0.0.1'
          openstack2:
            secret_key: MEGASECRET2
            source:
              engine: git
              address: https://repo1.domain.com/openstack/horizon.git
              rev: stable/icehouse
            plugin:
              contrail:
                app: contrail_openstack_dashboard
                override: true
                source:
                  type: git
                  address: git@repo1.domain.com:django/horizon-contrail.git
                  rev: develop
              monitoring:
                app: horizon_monitoring
                source:
                  type: git
                  address: git@domain.com:django/horizon-monitoring.git
                  rev: develop
              theme:
                app: bootswatch_theme
                source:
                  type: git
                  address: git@repo1.robotice.cz:django/horizon-bootswatch-theme.git
                  rev: develop
            cache:
              engine: 'memcached'
              host: '127.0.0.1'
              port: 11211
              prefix: 'CACHE_SITE2'
            api_versions:
              identity: 3
            identity:
              engine: 'keystone'
              host: '127.0.0.1'
              port: 5000
            mail:
              host: '127.0.0.1'

API versions override

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        app:
          openstack_api_overrride:
            secret_key: MEGASECRET1
            api_versions:
              identity: 3
              volume: 2
            source:
              engine: git
              address: https://github.com/openstack/horizon.git
              rev: stable/havana

Note: Keystone v3 domains not a good idea for ever - abandoned by devs. Policy files don't work, particularly cloud_admin:
https://blueprints.launchpad.net/horizon/+spec/domain-based-rbac

Control dashboard behaviour

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        app:
          openstack_dashboard_overrride:
            secret_key: password
            dashboards:
              settings:
                enabled: true
              project:
                enabled: false
                order: 10
              admin:
                enabled: false
                order: 20
            source:
              engine: git
              address: https://github.com/openstack/horizon.git
              rev: stable/juno

Enable WebSSO feature

.. code-block:: yaml

    horizon:
      server:
        enabled: true
        websso:
          login_url: "WEBROOT + 'auth/login/'"
          logout_url: "WEBROOT + 'auth/logout/'"
          websso_choices:
            - saml2
            - oidc


More Information
================

* https://github.com/openstack/horizon
* http://dijks.wordpress.com/2012/07/06/how-to-change-screen-resolution-of-novnc-client-in-openstack-essex-dashboard-nova-horizon/


Documentation and Bugs
======================

To learn how to install and update salt-formulas, consult the documentation
available online at:

    http://salt-formulas.readthedocs.io/

In the unfortunate event that bugs are discovered, they should be reported to
the appropriate issue tracker. Use Github issue tracker for specific salt
formula:

    https://github.com/salt-formulas/salt-formula-horizon/issues

For feature requests, bug reports or blueprints affecting entire ecosystem,
use Launchpad salt-formulas project:

    https://launchpad.net/salt-formulas

You can also join salt-formulas-users team and subscribe to mailing list:

    https://launchpad.net/~salt-formulas-users

Developers wishing to work on the salt-formulas projects should always base
their work on master branch and submit pull request against specific formula.

    https://github.com/salt-formulas/salt-formula-horizon

Any questions or feedback is always welcome so feel free to join our IRC
channel:

    #salt-formulas @ irc.freenode.net
