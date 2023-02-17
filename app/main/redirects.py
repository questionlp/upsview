# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2023 Linh Pham
# nutters is released under the terms of the MIT License
"""Main Redirect Routes for Nutters Web Application"""
from flask import Blueprint, url_for

from app.utility import redirect_url

blueprint = Blueprint("main_redirects", __name__)


@blueprint.route("/favicon.ico")
def favicon():
    """Redirect: /favicon.ico to /static/favicon.svg"""
    return redirect_url(url_for("static", filename="favicon.svg"))


@blueprint.route("/static/favicon.ico")
def static_favicon():
    """Redirect: /static/favicon.ico to /static/favicon.svg"""
    return redirect_url(url_for("static", filename="favicon.svg"))
