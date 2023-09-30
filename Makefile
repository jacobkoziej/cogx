# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2023  Jacob Koziej <jacobkoziej@gmail.com>

BLACK ?= black
BLACKFLAGS +=                       \
	--line-length 79            \
	--skip-string-normalization

MDFORMAT ?= mdformat
MDFORMATFLAGS +=  \
	--wrap 72

PIPCOMPILE ?= pip-compile
PIPCOMPILEFLAGS +=        \
	--allow-unsafe    \
	--generate-hashes \
	--no-strip-extras \
	--upgrade         \
	--verbose


.PHONY: all
all:


.PHONY: fmt
fmt:
	$(BLACK) $(BLACKFLAGS) .
	$(MDFORMAT) $(MDFORMATFLAGS) README.md


.PHONY: dev-requirements.txt
dev-requirements.txt:
	$(PIPCOMPILE) $(PIPCOMPILEFLAGS) --extra dev --output-file $@


.PHONY: requirements.txt
requirements.txt:
	$(PIPCOMPILE) $(PIPCOMPILEFLAGS) --output-file $@
