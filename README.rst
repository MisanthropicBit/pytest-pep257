PEP257 plugin for py.test 0.1.0
===============================

**This project is currently still in development!**

.. .. image:: https://travis-ci.org/MisanthropicBit/pep257_plugin.svg?branch=master
..     :target: https://travis-ci.org/MisanthropicBit/pep257_plugin

.. .. image:: https://pypip.in/v/pep257_plugin/badge.png
..     :target: https://crate.io/packages/pep257_plugin/
..     :alt: Latest PyPI version

A `py.test <http://pytest.org/latest/>`_ plugin for checking Python files for `PEP257 <http://legacy.python.org/dev/peps/pep-0257/>`_ compliance.
Inspired by the `pep8 plugin for pytest <https://bitbucket.org/hpk42/pytest-pep8/>`_.

Uses the  `pep257 static checker tool <https://github.com/GreenSteam/pep257>`_.

Installation:
-------------

You can install via `pip <http://pip.readthedocs.org/en/latest/index.html>`_:

    >>> pip install pytest-pep257

Alternatively, you can download this repository or clone it:

    >>> git clone https://www.github.com/MisanthropicBit/pep257_plugin.git

and then run:

    >>> python setup.py install

Usage:
------

Running ``py.test`` with the following option checks all collected Python files
for PEP257 compliance:

    >>> py.test --pep257 .
