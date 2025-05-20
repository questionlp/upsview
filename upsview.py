# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2025 Linh Pham
# upsview is released under the terms of the MIT License
"""Application Bootstrap Script for upsview Web Application."""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
