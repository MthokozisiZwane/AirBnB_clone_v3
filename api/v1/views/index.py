#!/usr/bin/python3
"""
import app_views from api.v1.views and creates a route
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
