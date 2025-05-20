# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2025 Linh Pham
# upsview is released under the terms of the MIT License
"""UPS Status and Information Retrieval Module."""

from typing import Any

import nut2


def retrieve_ups_info(
    host: str, port: int, login: str, password: str, ups_name: str
) -> dict[str, Any]:
    """Read UPS status and information using nut2 library."""
    if not host or not ups_name:
        return None

    nut_client = nut2.PyNUTClient(host=host, port=port, login=login, password=password)

    return nut_client.list_vars(ups_name)
