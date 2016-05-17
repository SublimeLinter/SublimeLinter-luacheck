#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Copyright (c) 2015 Peter Melnichenko
# Copyright (c) 2014 CorvisaCloud, LLC
#
# License: MIT
#

"""This module exports the Luacheck plugin class."""

from SublimeLinter.lint import Linter


class Luacheck(Linter):
    """Provides an interface to luacheck."""

    syntax = 'lua'
    cmd = 'luacheck - --formatter=plain --codes --ranges --filename @'

    version_args = '--help'
    version_re = r'[Ll]uacheck (?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.11.0, < 1.0.0'

    regex = (
        r'^.+:(?P<line>\d+):(?P<col>\d+)\-(?P<col_end>\d+): '
        r'\((?:(?P<error>E)|(?P<warning>W))\d+\) '
        r'(?P<message>.+)'
    )

    def split_match(self, match):
        """Patch regex matches to highlight token correctly."""
        match, line, col, error, warning, msg, _ = super().split_match(match)
        col_end = int(match.group(3))
        token_len = col_end - col
        return match, line, col, error, warning, msg, "." * token_len
