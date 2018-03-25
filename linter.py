from SublimeLinter.lint import Linter


class Luacheck(Linter):
    cmd = 'luacheck - --formatter=plain --codes --ranges --filename ${file}'
    regex = (
        r'^.+:(?P<line>\d+):(?P<col>\d+)\-(?P<col_end>\d+): '
        r'\((?:(?P<error>E\d+)|(?P<warning>W\d+))\) '
        r'(?P<message>.+)'
    )
    defaults = {
        'selector': 'source.lua'
    }

    def split_match(self, match):
        """Patch regex matches to highlight token correctly."""
        match, line, col, error, warning, msg, _ = super().split_match(match)
        col_end = int(match.group(3))
        token_len = col_end - col
        return match, line, col, error, warning, msg, "." * token_len
