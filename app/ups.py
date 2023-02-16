# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2022 Linh Pham
"""UPS Status and Information Retrieve Module"""

from typing import Any, Dict

import nut2


def retrieve_ups_info(
    host: str, port: int, login: str, password: str, ups_name: str
) -> Dict[str, Any]:
    """Read UPS status and information using nut2 library"""
    if not host or not ups_name:
        return

    nut_client = nut2.PyNUTClient(host=host, port=port, login=login, password=password)

    return nut_client.list_vars(ups_name)