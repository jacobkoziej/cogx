# SPDX-License-Identifier: GPL-3.0-or-later
#
# cog.py -- cog wrapper
# Copyright (C) 2023  Jacob Koziej <jacobkoziej@gmail.com>

import typing


class Cogless:
    _instance = None

    inFile: typing.Final[str] = ''
    outFile: typing.Final[str] = ''
    firstLineNum: typing.Final[int] = -1

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cogless, cls).__new__(cls)

        return cls._instance

    @classmethod
    def error(*args, **kwargs) -> None:
        pass

    @classmethod
    def msg(*args, **kwargs) -> None:
        pass

    @classmethod
    def out(*args, **kwargs) -> None:
        pass

    @classmethod
    def outl(*args, **kwargs) -> None:
        pass


class Cog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Cog, cls).__new__(cls)

        return cls._instance

    def __init__(self, *, cog: typing.Any = None) -> None:
        if cog is None:
            try:
                import cog as _cog

                self._cog = _cog

            except ModuleNotFoundError:
                self._cog = Cogless()
        else:
            self._cog = cog

    @property
    def IN_FILE(self) -> str:
        return self._cog.inFile

    @property
    def OUT_FILE(self) -> str:
        return self._cog.outFile

    @property
    def LINE_NUMBER(self) -> str:
        return self._cog.firstLineNum

    def error(self, *args, **kwargs) -> None:
        self._cog.error(*args, **kwargs)

    def msg(self, *args, **kwargs) -> None:
        self._cog.msg(*args, **kwargs)

    def out(self, *args, **kwargs) -> None:
        self._cog.out(*args, **kwargs)

    def outl(self, *args, **kwargs) -> None:
        self._cog.outl(*args, **kwargs)


del typing
