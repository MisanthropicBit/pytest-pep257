"""Setup and distribution file for the pytest pep257 plugin."""

# PEP257 -- Docstring Conventions
# http://legacy.python.org/dev/peps/pep-0257/

from __future__ import with_statement
from setuptools import setup

__date__ = '2014-06-15'  # YYYY-MM-DD


def get_version(filename):
    with open(filename) as fh:
        for line in fh:
            if line.startswith('__version__'):
                return line.split('=')[-1].strip()[1:-1]


setup(
    name="pytest-pep257",
    version=get_version('plugin.py'),
    install_requires=['pytest', 'pytest-cache', 'pep257'],
    author='Alexander Bock',
    author_email='alexander.asp.bock@gmail.com',
    py_modules=['plugin'],
    platforms="Platform independent",
    description='Plugin for py.test enabling PEP257 compliance checks',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='pytest pep257 plugin',
    url='https://github.com/MisanthropicBit/pytest-pep257',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Testing'
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ],

    # Necessary so pytest can find the plugin
    entry_points={
        'pytest11': [
            'pytest-pep257 = plugin'
        ]
    }
)
