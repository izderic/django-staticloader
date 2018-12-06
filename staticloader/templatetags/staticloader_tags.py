from django import template
from django.conf import settings
from staticloader.main import render

register = template.Library()


@register.simple_tag
def loadjs(*args):
    """
    Returns rendered script tag(s) with the specified js file path(s).
    """
    return render(settings, 'JS_FILES', 'staticloader/load_js.html', *args)


@register.simple_tag
def loadcss(*args):
    """
    Returns rendered link tag(s) with the specified css file path(s).
    """
    return render(settings, 'CSS_FILES', 'staticloader/load_css.html', *args)
