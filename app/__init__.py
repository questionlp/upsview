# vim: set noai syntax=python ts=4 sw=4:
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022-2025 Linh Pham
# upsview is released under the terms of the MIT License
"""Core Application for upsview Web Application."""
from flask import Flask

from app import devices, mappings
from app.errors import handlers
from app.main.redirects import blueprint as redirects_bp
from app.main.routes import blueprint as main_bp
from app.version import APP_VERSION


def create_app():
    """Create and initialize Flask app."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Override base Jinja options
    app.jinja_options = Flask.jinja_options.copy()
    app.jinja_options.update({"trim_blocks": True, "lstrip_blocks": True})
    app.create_jinja_environment()

    # Register error handlers
    app.register_error_handler(404, handlers.not_found)
    app.register_error_handler(500, handlers.handle_exception)

    # Load configuration file
    app.config["devices"] = devices.load_devices()
    app.config["mappings"] = mappings.load_mappings()

    # Set up Jinja globals
    app.jinja_env.globals["app_version"] = APP_VERSION

    # Register application blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(redirects_bp)

    return app
