from setuptools import setup
import sys, os

version = '0.1.0'

setup(
    name = 'cmddict',
    version = version,
    description = 'bilingual dictionary in command line',
    long_description = 'bilingual dictionary in command line',
    classifier = [],
    author = 'Xuyan',
    author_email = 'lelielru@gmail.com',
    url = 'https://github.com/Tacsy/cmddict',
    license = 'MIT',
    install_requires = ['termcolor']
)