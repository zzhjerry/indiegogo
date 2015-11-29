#!/usr/bin/python

from setuptools import setup

setup(
    name = 'indiegogo',
    version = '0.0.1',
    author = 'Jerry Zhang',
    author_email = 'zzh699@gmail.com',
    description = 'Use indiegogo api with python objects',
    license = 'BSD',
    keywords = 'indiegogo',
    packages = ['indiegogo'],
    install_requires = ['requests>=0.14.0'],
)
