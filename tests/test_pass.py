#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Remembered the module's doc-string."""  # D100: Missing module doc-string

import sys
import pytest


# Missing doc-string from method class
class pass_D101(object):

    """D100 at public class level."""

    def pass_D102(self):
        """Doc-string from public method."""
        pass


def pass_D103():
    """Doc-string from public function.

    D203, D204: Blank lines before and after public function

    """
    pass


def pass_D209():
    """Multi-line doc-string should be...

    ...on separate lines.

    """


def pass_D301():
    r"""Use raw string literals if any backslashes are present.

    Like this \

    """
    pass


@pytest.mark.skipif(sys.version_info[0] >= 3,
                    reason='Test only valid for Python 2')
def pass_D302():
    u"""Use Unicode string literals if there are any Unicode characters...

    ...in your strîng

    """
    pass


def pass_D401():
    """Use imperative descriptions."""
    pass
