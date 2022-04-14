# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2022 Linh Pham
"""Main Routes for Nutters Web Application"""
from datetime import datetime
from flask import Blueprint, Response, current_app, render_template, send_file

from app.ups import retrieve_ups_info

blueprint = Blueprint("main", __name__)


@blueprint.route("/")
def index():
    """Landing Page"""
    devices = {}
    for device in current_app.config["devices"]:
        ups_info = retrieve_ups_info(
            host=device["host"],
            port=device["port"],
            login=device["login"],
            password=device["password"],
            ups_name=device["ups_name"],
        )

        if ups_info:
            devices[device["alias"]] = ups_info

    rendered_at = datetime.now()
    return render_template(
        "index.html",
        devices=devices,
        mappings=current_app.config["mappings"],
        rendered_at=f"{rendered_at:%Y-%m-%d %H:%M:%S}",
    )
