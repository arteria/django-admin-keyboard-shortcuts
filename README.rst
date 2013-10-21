Django Admin Keyboard Shortcuts
============

Keyboard Shortcuts for your Admin Backend

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-admin-keyboard-shortcuts

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/arteria/django-admin-keyboard-shortcuts.git#egg=admin_keyboard_shortcuts

TODO: Describe further installation steps (edit / remove the examples below):

Add ``admin_keyboard_shortcuts`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'admin_keyboard_shortcuts',
    )

Add the ``admin_keyboard_shortcuts`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^app-url/', include('admin_keyboard_shortcuts.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load admin_keyboard_shortcuts_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate admin_keyboard_shortcuts


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Icon
----

The icon is from Janik Baumgartner http://janikbaumgartner.com/
and can be found here: http://www.iconarchive.com/show/woocons-icons-by-janik-baumgartner.html

Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-admin-keyboard-shortcuts
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
