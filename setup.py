"""
Package configuration file
"""
from distutils.core import setup
from setuptools import find_packages

setup(
    name='pylint-mccabe',
    version='0.1.0',
    author='Infoxchange Australia dev team',
    author_email='devs@infoxchange.net.au',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/pylint-mccabe/',
    license='MIT',
    description='McCabe complexity checker as a PyLint plugin',
    long_description=open('README.rst').read(),
    install_requires=[
        'mccabe >= 0.2',
        'pep8 >= 1.4.5',
        'pylint >= 0.28.0',
    ],
)
