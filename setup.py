# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    version='v0.0.1',
    name='django-tastypie-sepomex',
    packages=find_packages(),
    description='Little django application that exposes the sepomex database in a RESTful way.',
    url='https://github.com/slackmart/tastypie-sepomex',
    keywords=['sepomex', 'tastypie', 'django'],
    install_requires=[
        'django-tastypie'
    ],
    license='MIT'
)
