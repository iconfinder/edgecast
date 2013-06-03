#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'edgecast',
    'django_edgecast',
]

requires = [
    'requests>=1.0.0,<2.0.0',
]

tests_require = [
    'nose',
    'rednose',
    'pep8',
]

setup(
    name='edgecast',
    version='1.0.2',
    description='Convenient EdgeCast CDN management for Python',
    author='Nick Bruun',
    author_email='nick@bruun.co',
    url='http://bruun.co/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={
        'edgecast': 'edgecast',
        'django_edgecast': 'django_edgecast',
    },
    include_package_data=True,
    tests_require=tests_require,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=True,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
