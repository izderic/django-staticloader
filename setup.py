import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-staticloader',
    version='0.1',
    packages=['staticloader'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app which provides template tags for loading JavaScript and CSS files into the template.',
    long_description=README,
    url='http://www.example.com/',
    author='Ivan Zderic',
    author_email='ivan_zderic@hotmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
)