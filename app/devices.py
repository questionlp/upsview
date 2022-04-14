# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2022 Linh Pham
"""Devices Configuration File Loading for Nutters Web Application"""
import json
from typing import Any, Dict


def load_devices(devices_file_path: str = "devices.json") -> Dict[str, Dict[str, Any]]:
    with open(devices_file_path, "r") as devices_file:
        devices_config = json.load(devices_file)

    if "devices" in devices_config:
        return devices_config["devices"]
