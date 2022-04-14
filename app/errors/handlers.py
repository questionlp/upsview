# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
"""Error Handlers Module for Nutters Web Application"""
from flask import render_template


def not_found(error):
    """Handle resource not found conditions"""
    return render_template("errors/404.html"), 404


def handle_exception(error):
    """Handle exceptions in a slightly more graceful manner"""
    return render_template("errors/500.html", error=error), 500
