===================
django-staticloader
===================

Staticloader is a simple Django app which provides template tags for loading JavaScript and CSS files into the template.

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
            'jquery': 'jquery-1.11.3.min.js',
            'bootstrap': 'bootstrap-3.2.0-dist/js/bootstrap.min.js',
            ...
        }

        CSS_FILES = {
            'style': 'css/style.css',
            'bootstrap': 'bootstrap-3.2.0-dist/css/bootstrap.min.css',
            ...
        }

3. In your template add ``{% load staticloader_tags %}`` on the top.

4. Use template tags ``{% loadjs %}`` and ``{% loadcss %}`` to include the files defined in settings.

    .. code:: python

        {% loadcss "style" "bootstrap" %}
        {% loadjs "jquery" "bootstrap" %}