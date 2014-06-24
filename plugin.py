# -*- coding: utf-8 -*-

"""A pep257 plugin for py.test."""

__author__ = 'Alexander Bock'
__version__ = '0.1.0'
__license__ = 'MIT'
__date__ = '2014-06-16'  # YYYY-MM-DD

import sys
import pytest
import pep257

# Cache key for pytest.cache for saving file modification times 
CACHE_KEY = 'pep257/mtimes'


class PEP257Error(Exception):

    """Base exception for PEP 257-related errors."""

    pass


class PEP257Item(pytest.Item, pytest.File):

    """Represents a PEP 257 item."""

    _expected_errors = (EnvironmentError, pep257.AllError, SyntaxError)

    def __init__(self, path, parent, ignorelist):
        super(PEP257Item, self).__init__(path, parent)
        self.add_marker('pep257')

        print(ignorelist)

        self.ignorelist = ignorelist

    def setup(self):
        # Record file 'last modified' time
        self._mtime = self.fspath.mtime()
        old = self.config._pep257mtimes.get(str(self.fspath), (0, []))

        # If the old cache values correpsond to the current, do not check the
        # file again, as it passed previous PEP257 checks
        if old == (self._mtime, self.ignorelist):
            pytest.skip("File(s) previously passed PEP257 compliance")

    def runtest(self):
        """Run the pep257 checker on collected file."""
        # Get a list of all pep257.Errors
        temp = list(pep257.check([str(self.fspath)], ignore=self.ignorelist))

        if temp:
            raise PEP257Error(temp)

    def repr_failure(self, excinfo):
        """Report a PEP257 related failure."""
        if excinfo.errisinstance(PEP257Error):
            return "\n".join(map(str, excinfo.value.args[0]))

        return super(PEP257Item, self).repr_failure(excinfo)

    def reportinfo(self):
        """Report information about PEP257 checks and ignored errors."""
        ignores = ''

        if self.ignorelist:
            ignores = ' (ignoring %s)' % ', '.join(self.ignorelist)

        return (self.fspath, -1, "PEP257")


######################################################################
#
# py.test plugin hooks
#
######################################################################

######################################################################
# Configuration hooks
######################################################################
def pytest_addoption(parser):
    """Add plugin-specific optional arguments."""
    group = parser.getgroup('pep257', 'Check Python files for PEP257 '
        'compliance')

    group.addoption('--pep257', action='store_true',
                    help="Validate that Python sources conform to PEP257")

    # Add all pep257 options
    # group.addoption('--explain', action='store_true',
    #                 help='show explanation of each error')
    # group.addoption('--source', action='store_true',
    #                 help='show source for each error')
    # group.addoption('--ignore', metavar='<codes>', default='',
    #                 help='ignore a list comma-separated error codes, '
    #                      'for example: --ignore=D101,D202')

    # Add ini-file ignore rules
    parser.addini('pep257ignore', type='linelist',
                  help='List of PEP257 error codes to ignore')


def pytest_sessionstart(session):
    if session.config.option.pep257:
        # Hacky, but works (find a better way!)
        # pep257.Error.explain = session.config.option.explain
        # pep257.Error.source = session.config.option.source
        session.config._pep257ignore = session.config.getini("pep257-ignore")
        session.config._pep257mtimes = session.config.cache.get(CACHE_KEY, {})
    # else:
    #     if session.config.option.explain:
    #         session.config.warn("--explain only applicable with --pep257")

    #     if session.config.option.source:
    #         session.config.warn("--source only applicable with --pep257")


def pytest_sessionfinish(session):
    if hasattr(session.config, '_pep257mtimes'):
        session.config.cache.set(CACHE_KEY, session.config._pep257mtimes)
        del session.config._pep257mtimes


######################################################################
# Collection hooks
######################################################################
def pytest_collect_file(path, parent):
    if parent.config.option.pep257 and path.ext == '.py':
        return PEP257Item(path, parent, [])


######################################################################
# Reporting hooks
######################################################################
def pytest_runtest_logreport(report):
    pass
