Django Admin Keyboard Shortcuts
============

Keyboard Shortcuts for your Admin Backend. Currently, only a "save" shortcut is implemented.


Installation
------------

To get the latest stable release from PyPi 

.. code-block:: bash

    pip install django-admin-keyboard-shortcuts

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/arteria/django-admin-keyboard-shortcuts.git#egg=admin_keyboard_shortcuts

 
There are not further dependencies! 

Add ``admin_keyboard_shortcuts`` to your ``INSTALLED_APPS`` before ``django.contrib.admin``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'admin_keyboard_shortcuts',
		'django.contrib.admin', 
		...,
    )

 


Don't forget to collect the icons

.. code-block:: bash

    ./manage.py collectstatic


Usage
-----

Just hit 'cmd' + 's' (or 'Ctrl' + 's') instead of clicking  the "save" button on the bottom of the Django admin.


Icon
----

The icon is from Janik Baumgartner http://janikbaumgartner.com/
and can be found here: http://www.iconarchive.com/show/woocons-icons-by-janik-baumgartner.html

Contribute
----------

That's easy - just send your pull request. Thanks!