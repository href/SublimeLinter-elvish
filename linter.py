from SublimeLinter.lint import Linter
from SublimeLinter.lint.util import STREAM_STDERR


class Elvish(Linter):
    cmd = 'elvish -compileonly -norc'

    regex = (
        r"Compilation error: (?P<message>[^\n]+)\n"
        r".*\.elv, line (?P<line>[0-9]+)"
    )

    multiline = True

    # Elvish is capable of compiling from stdin, but it'll ignore the last
    # line if it doesn't end with a newline. Using a file works.
    tempfile_suffix = '.elv'

    error_stream = STREAM_STDERR

    defaults = {
        'selector': 'source.elvish'
    }
