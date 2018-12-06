===================
django-staticloader
===================

Staticloader is a simple Django app which provides template tags for loading JavaScript and CSS files into the template.

Installation
------------

Install using pip:

    ``pip install git+git://github.com/izderic/django-staticloader.git``

Quick start
-----------

1. Add "staticloader" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'staticloader',
    )

2. Define dictionaries ``JS_FILES`` and ``CSS_FILES`` in your Django settings file like this:

    .. code:: python

        # settings.py
        # ============

        JS_FILES = {
            'myCustomScript': 'js/myCustomScript.js',
            'exampleScript': 'js/exampleScript.js',
            ...
        }

        CSS_FILES = {
            'style': 'css/style.css',
            'otherStyle': 'css/otherStyle.css',
            ...
        }

3. In your template add ``{% load staticloader_tags %}`` on the top.

4. Use template tags ``{% loadjs %}`` and ``{% loadcss %}`` to include the files defined in settings.

    .. code:: python

        {% loadcss "style" "otherStyle" %}
        {% loadjs "myCustomScript" "exampleScript" %}

