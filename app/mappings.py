# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2022 Linh Pham
"""Mappings File Loading for Nutters Web Application"""
import json
from typing import Any, Dict


def load_mappings(
    mappings_file_path: str = "mappings.json",
) -> Dict[str, Dict[str, Any]]:
    with open(mappings_file_path, "r") as mappings_file:
        mappings = json.load(mappings_file)

    if "mappings" in mappings:
        return mappings["mappings"]
