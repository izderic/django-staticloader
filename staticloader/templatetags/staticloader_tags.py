from django import template
from django.template.loader import get_template
from django.conf import settings


register = template.Library()


def render_tag(template_name, file_paths):
    """
    Renders the specified template with given context.
    """
    template_obj = get_template(template_name)
    return template_obj.render({'files': file_paths})


@register.simple_tag
def loadjs(*args):
    """
    Returns rendered script tag(s) with the specified js file path(s).
    """
    files = [settings.JS_FILES.get(item) for item in args]
    return render_tag('staticloader/load_js.html', files)


@register.simple_tag
def loadcss(*args):
    """
    Returns rendered link tag(s) with the specified css file path(s).
    """
    files = [settings.CSS_FILES.get(item) for item in args]
    return render_tag('staticloader/load_css.html', files)
