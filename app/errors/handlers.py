# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2023 Linh Pham
# upsview is released under the terms of the MIT License
"""Error Handlers Module for upsview Web Application."""
from flask import render_template


def not_found(error):
    """Handle resource not found conditions."""
    return render_template("errors/404.html"), 404


def handle_exception(error):
    """Handle exceptions in a slightly more graceful manner."""
    return render_template("errors/500.html", error=error), 500
