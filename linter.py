#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Copyright (c) 2014 CorvisaCloud, LLC
#
# License: MIT
#

"""This module exports the Luacheck plugin class."""

from SublimeLinter.lint import Linter


class Luacheck(Linter):

    """Provides an interface to luacheck."""

    syntax = 'lua'
    tempfile_suffix = 'lua'
    defaults = {
        '--ignore:,': ['channel'],
        '--only:,': [],
        '--limit=': None,
        '--globals:,': [],
    }
    comment_re = r'\s*--'
    inline_settings = 'limit'
    inline_overrides = ('ignore', 'only', 'globals')
    cmd = 'luacheck @ *'
    regex = r'^(?P<filename>.+):(?P<line>\d+):(?P<col>\d+): (?P<message>.*)$'

    def build_args(self, settings):
        """Return args, transforming --ignore, --only, and --globals args into a format luacheck understands."""
        args = super().build_args(settings)

        for arg in ('--ignore', '--only', '--globals'):
            try:
                index = args.index(arg)
                values = args[index + 1].split(',')
                args[index + 1:index + 2] = values
            except ValueError:
                pass

        return args
