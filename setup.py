#!/usr/bin/env python

""" modem-cmd installation script """

VERSION = '1.0.2'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.readlines()

setup(
    name='modem-cmd',
    version='{0}'.format(VERSION),
    description='Send arbitrary AT commands to your modem',
    license='GPLv3+',
    author='Antony Shen',
    author_email='shih@yulun.me',
    url='https://github.com/antonyshen/modem-cmd',
    download_url=(
        'https://github.com/antonyshen/modem-cmd/archive/{0}.tar.gz'
            .format(VERSION),
    ),
    keywords=['modem', 'at commands', 'serial'],
    packages=['modemcmd'],
    scripts=['bin/atc.py'],
    install_requires=requires,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware',
        'Topic :: Terminals :: Serial',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
