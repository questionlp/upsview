# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2022 Linh Pham
"""Application Bootstrap Script for Nutters Web Application"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
