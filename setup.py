# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    version='v0.0.1',
    name='django-sepomex',
    packages=find_packages(),
    install_requires=[
        'django-tastypie'
    ],
    license='MIT'
)
