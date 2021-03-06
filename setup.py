"""
Package configuration file
"""
from setuptools import setup

setup(
    name='pylint-mccabe',
    version='0.1.3',
    author='Infoxchange Australia dev team',
    author_email='devs@infoxchange.net.au',
    py_modules=['pylint_mccabe'],
    url='http://pypi.python.org/pypi/pylint-mccabe/',
    license='MIT',
    description='McCabe complexity checker as a PyLint plugin',
    long_description=open('README.rst').read(),
    install_requires=[
        'mccabe >= 0.2',
        'pep8 >= 1.4.6',
        'pylint >= 0.28.0',
    ],
)
