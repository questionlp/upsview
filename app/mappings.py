# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2023 Linh Pham
# nutters is released under the terms of the MIT License
"""Mappings File Loading for Nutters Web Application"""
import json
from pathlib import Path
from typing import Any, Dict


def load_mappings(
    mapping_file_path: str = "mappings.json",
) -> Dict[str, Dict[str, Any]]:
    fallback_mapping_file = "mappings.json.dist"

    if mapping_file_path and not Path(mapping_file_path).exists():
        if Path(fallback_mapping_file).exists():
            mapping_file_path = fallback_mapping_file
        else:
            return None

    if Path(mapping_file_path).exists():
        with open(mapping_file_path, "r") as mapping_file:
            mappings = json.load(mapping_file)

        if "mappings" in mappings:
            return mappings["mappings"]

    return None
