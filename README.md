A Django Admin Keyboard Shortcuts Experiment
============

Consider this app as an experiment that was abandoned. Do not use it in production. The idea behind this experiment was to provide keyboard shortcuts for your admin site. See "Usage" section below for all implemented shortcuts. 


Installation
============

To get the latest stable release from PyPi 

.. code-block:: bash

    pip install django-admin-keyboard-shortcuts

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/arteria/django-admin-keyboard-shortcuts.git#egg=admin_keyboard_shortcuts

 
There are not further dependencies! 

In your project settings, add ``admin_keyboard_shortcuts`` to your ``INSTALLED_APPS`` before ``django.contrib.admin``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'admin_keyboard_shortcuts',
        'django.contrib.admin', 
        ...,
    )
   


Optionally, by setting ``ADMIN_KEYBOARD_SHORTCUTS_HIDE_ICON = True`` in project settings, the icon that indicates 
"shortcut support" will be hidden. 

 


Don't forget to collect the icons

.. code-block:: bash

    ./manage.py collectstatic


Usage
============

Keyboard Shortcut or Key  | Alternative Keyboard Shortcut | Page | Command
 ------------- | ------------- | ------------- | -------------
``Ctrl`` + ``s`` |   ``cmd`` + ``s``  |  Object detail | Save the current object. Is equal to clicking the "save" button on the bottom of page.
 ``j`` / ``k`` | | Object list | Navigation up and down in the result list. Pressing the ``return`` key on a selected row opens the object detail page.
``Ctrl`` + ``o`` |   ``cmd`` + ``o``  |  Object detail | Save current and open new object (= add another). 
``Ctrl`` + ``c`` |   ``cmd`` + ``c``  |  Object detail | Save current and and continue editing. 

TODO and planned features
============

* Open new object (= add another) on the for result lists
* Navigation using ``j`` and ``k`` in admin start page.


Icon
============


The icon is from Janik Baumgartner http://janikbaumgartner.com/
and can be found here: http://www.iconarchive.com/show/woocons-icons-by-janik-baumgartner.html

History
============


Development Version
-------------------

0.1.5
-----

* Bugfix release

0.1.4
-----

* Added new shortcuts, see Usage section.
* Changed README to Markdown 
* Startet History



Contribute
============


That's easy - just send your pull request. Thanks!

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/philippeowagner/django-admin-keyboard-shortcuts/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

