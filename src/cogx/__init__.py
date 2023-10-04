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


del os
del typing
