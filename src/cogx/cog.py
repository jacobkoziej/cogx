# SPDX-License-Identifier: GPL-3.0-or-later
#
# cog.py -- cog wrapper
# Copyright (C) 2023  Jacob Koziej <jacobkoziej@gmail.com>

try:
    from cog import *

    import typing

    IN_FILE: typing.Final[str] = inFile
    OUT_FILE: typing.Final[str] = outFile

    del inFile
    del outFile

    first_line_number: int = firstLineNum

    del firstLineNum

    del typing

except ModuleNotFoundError:
    IN_FILE: str = ''
    OUT_FILE: str = ''

    first_line_number: int = 1

    def error(msg: str) -> None:
        pass

    def msg(msg: str) -> None:
        pass

    def out(msg: str) -> None:
        pass

    def outl(msg: str) -> None:
        pass
