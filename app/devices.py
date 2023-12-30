# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2023 Linh Pham
# upsview is released under the terms of the MIT License
"""Devices Configuration File Loading for upsview Web Application."""
import json
from pathlib import Path
from typing import Any, Dict


def load_devices(devices_file_path: str = "devices.json") -> Dict[str, Dict[str, Any]]:
    if devices_file_path and Path(devices_file_path).exists():
        with Path(devices_file_path).open(mode="r", encoding="utf-8") as devices_file:
            devices_config = json.load(devices_file)

        if "devices" in devices_config:
            return devices_config["devices"]

    return None
