from django.test import SimpleTestCase
from django.template import Context, Template

from staticloader.main import render
from staticloader.exceptions import SettingDoesNotExist, NotDictException, ContainsDuplicatesException
from staticloader.utils import Settings


SAMPLE_DATA = [
    {
        'myCustomScript': 'js/myCustomScript.js',
        'exampleScript': 'js/exampleScript.js'
    },
    {
        'style': 'css/style.css',
        'otherStyle': 'css/otherStyle.css'
    }
]


class RenderTestCase(SimpleTestCase):

    def test_does_not_exist(self):
        settings = Settings(*SAMPLE_DATA)
        delattr(settings, 'JS_FILES')
        self.assertRaises(SettingDoesNotExist, render, settings, 'JS_FILES', 'staticloader/load_js.html', 'jquery')

    def test_not_dict(self):
        settings = Settings('Not dict', 'Not dict')
        self.assertRaises(NotDictException, render, settings, 'JS_FILES', 'staticloader/load_js.html', 'jquery')

    def test_duplicates(self):
        settings = Settings(*SAMPLE_DATA)
        self.assertRaises(ContainsDuplicatesException, render, settings, 'JS_FILES', 'staticloader/load_js.html', 'jquery', 'jquery')

    def test_js(self):
        settings = Settings(*SAMPLE_DATA)
        html = render(settings, 'JS_FILES', 'staticloader/load_js.html', 'myCustomScript')
        self.assertIn('<script type="text/javascript" src="/static/js/myCustomScript.js"></script>', html)

    def test_css(self):
        settings = Settings(*SAMPLE_DATA)
        html = render(settings, 'CSS_FILES', 'staticloader/load_css.html', 'style')
        self.assertIn('<link rel="stylesheet" href="/static/css/style.css">', html)
