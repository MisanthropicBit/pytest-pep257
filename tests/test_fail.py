#!/usr/bin/env python
# -*- coding: utf-8 -*-

# D100: Missing module doc-string

import sys
import pytest


# Missing doc-string from method class
class fail_D101(object):
    def fail_D102(self):
        # Missing doc-string from public method
        pass


def fail_D103():  # Missing doc-string from public function
    pass


def fail_D203():

    """There should not be any blank lines before this doc-string."""
    pass


def fail_D204():
    """There should not be any blank lines after this doc-string."""

    pass


def fail_D205():
    """This is the summary.

    This is the more comprehensive description
    """
    pass


def fail_D206():
    """Docstring should be indented with spaces, not tabs."""
    pass


def fail_D207():
   """Doc-string under-indented."""


def fail_D208():
     """Doc-string over-indented."""


def fail_D209():
    """Multi-line doc-string should be\non separate lines."""


def fail_D300():
    '''D300: Use double-quotes.'''
    pass


def fail_D301():
    """Use raw string literals if there are any backslashes in your doc-string.

    Like this \

    """


@pytest.mark.skipif(sys.version_info[0] >= 3,
                    reason='Test only valid for Python 2')
def fail_D302():
    """Use Unicode string literals if there are any Unicode characters...

    ...in your strîng

    """
    pass


def fail_D400():
    """The first line should end with a period"""
    pass


def fail_D401():
    """Uses 'uses' instead of imperative 'use'."""
    pass


def fail_D402():
    """Do not use function signature fail_D402 -> returns None."""
    pass
