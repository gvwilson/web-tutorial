"""Serve data from data model layer."""

from flask import Flask, abort, jsonify, make_response, redirect, request, url_for
from flask_cors import CORS
import random
import string

import models
import views
from util import AppException, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL


COOKIE_NAME = "wp4ds"
HEARTBEAT = {"message": "alive"}
RANDOM_LEN = 8


def create_app():
    """Build application and configure routes."""
    app = Flask("err")
    CORS(app)
    app.config["cookie_value"] = "".join(random.choices(string.ascii_lowercase, k=RANDOM_LEN))

    @app.get("/")
    def root():
        try:
            return views.all_staff(models.all_staff())
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving all staff: {exc}")

    @app.post("/login")
    def login_handler():
        """Accept password and go back home."""
        username = request.form["username"]
        password = request.form["password"]
        response = make_response(redirect(url_for("root")))
        if username and password:
            response.set_cookie(COOKIE_NAME, app.config["cookie_value"])
        else:
            response.set_cookie(COOKIE_NAME, "", expires=0)
        return response

    @app.get("/exp/<staff_id>")
    def exp(staff_id):
        try:
            if request.cookies.get(COOKIE_NAME) == app.config["cookie_value"]:
                return views.experiments(models.experiments(staff_id), staff_id)
            else:
                abort(HTTP_403_NOT_AUTHORIZED)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving experiments for {staff_id}: {exc}")

    @app.get("/heartbeat")
    def heartbeat():
        try:
            return views.heartbeat(HEARTBEAT)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving heartbeat: {exc}")

    return app
