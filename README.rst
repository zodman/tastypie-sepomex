*****************
Tastypie Sepomex
*****************

Little django application that exposes the sepomex database in a RESTful way.

.. image:: https://api.travis-ci.org/slackmart/tastypie-sepomex.svg?branch=master
    :target: https://travis-ci.org/slackmart/tastypie-sepomex

.. image:: https://coveralls.io/repos/slackmart/tastypie-sepomex/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/slackmart/tastypie-sepomex?branch=master 

Installation
============

::

    $ pip install django-tastypie-sepomex

Configuration
=============

1. Once installed, you must add `sepomex` to your `INSTALLED_APPS`

::

    INSTALLED_APPS += ['sepomex']

2. Apply migrate command to add the sepomex models to your database.

::

    $ python manage.py migrate sepomex

3. Populate your sepomex models

::

    $ python manage.py loadsepomex

This command will call the `loadmxstates` and `loadmxmunicipalities` commands. It finally will fill the `sepomex_mxasentamiento` table to complete the process.

Run your server
===============

::

    $ python manage.py runserver


... and use the endpoints provided
==================================

Get the list of states
----------------------

There are 32 states, so we pass that as a query string.

::

    $ curl localhost:8000/api/v1/mxestado/?limit=32

List first 20 municipalities for Coahuila
-----------------------------------------

Coahuila's id is 5. If not specified, the limit objects per query is 20

::

    $ curl localhost:8000/api/v1/mxmunicipio/?mx_estado__id=5
