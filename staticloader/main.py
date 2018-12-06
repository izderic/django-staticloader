from django.template.loader import get_template

from staticloader.exceptions import SettingDoesNotExist, NotDictException, ContainsDuplicatesException
from staticloader.utils import contains_duplicates


def render_tag(template_name, file_paths):
    """
    Renders the specified template with given context.
    """
    template_obj = get_template(template_name)
    return template_obj.render({'files': file_paths})


def render(django_settings, settings_var, template, *args):
    files = getattr(django_settings, settings_var, None)

    if files is None:
        raise SettingDoesNotExist('Please define {} dict in your settings file.'.format(settings_var))

    files_type = type(files)
    if files_type is not dict:
        raise NotDictException('{} must be dictionary. It is type of {}.'.format(settings_var, files_type.__name__))

    if contains_duplicates(args):
        raise ContainsDuplicatesException('Please remove duplicate items.')

    return render_tag(template, [files.get(item) for item in args])
