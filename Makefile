# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2023  Jacob Koziej <jacobkoziej@gmail.com>

PIPCOMPILE ?= pip-compile
PIPCOMPILEFLAGS +=        \
	--allow-unsafe    \
	--generate-hashes \
	--no-strip-extras \
	--upgrade         \
	--verbose


.PHONY: all
all:


.PHONY: dev-requirements.txt
dev-requirements.txt:
	$(PIPCOMPILE) $(PIPCOMPILEFLAGS) --extra dev --output-file $@


.PHONY: requirements.txt
requirements.txt:
	$(PIPCOMPILE) $(PIPCOMPILEFLAGS) --output-file $@
