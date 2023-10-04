# SPDX-License-Identifier: GPL-3.0-or-later
#
# __init__.py -- cog extensions
# Copyright (C) 2023  Jacob Koziej <jacobkoziej@gmail.com>

import os
import typing

from . import cog

cog = cog.Cog()


__author__: typing.Final[str] = 'Jacob Koziej'
__version__: typing.Final[str] = '0.0.0'


DIRNAME: typing.Final[str] = os.path.dirname(cog.IN_FILE)


def cat(files: list[str], *, relative: bool = True) -> None:
    import os

    if relative:
        files = [os.path.join(DIRNAME, file) for file in files]

    output: list[str] = []

    for file in files:
        with open(file) as f:
            output += [f.read()]

    cog.out('\n'.join(output))


del os
del typing
