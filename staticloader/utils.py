class Settings(object):
    """Simulates Django settings"""
    def __init__(self, js_files, css_files):
        self.JS_FILES = js_files
        self.CSS_FILES = css_files


def contains_duplicates(list_object):
    return len(list_object) != len(set(list_object))
