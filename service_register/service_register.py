import json

import requests
from flask import Flask, Request, Response

# May be more lightweight since clients will request the content
FLAG_USE_REDIRECT = True

_services = {}
app = Flask(__name__)


def get_request() -> Request:
    import flask
    return flask.request


@app.route("/", methods=["GET"])
def _list():
    response = Response()
    response.data = json.dumps(_services, indent=2)
    response.status_code = 200
    return response


@app.route("/<string:name>", methods=["GET"])
def _fetch(name: str):
    request = get_request()
    response = Response()
    service: dict = _services.get(name)

    if service:
        url = "http://{ip}:{port}{path}".format(**service)

        if FLAG_USE_REDIRECT:
            # Using redirect
            response.status_code = 302
            response.data = request.data
            response.headers = dict(request.headers)
            response.location = url
        else:
            # Executing the request
            content = requests.get(url)
            response.headers = dict(content.headers)
            response.status_code = content.status_code
            response.data = content.content
    else:
        response.status_code = 404

    return response


@app.route("/<string:name>", methods=["POST"])
def _register(name: str):
    request = get_request()
    request_json: dict = request.json
    response = Response()

    if name in _services:
        response.status_code = 409
        return response

    if not request_json:
        response.status_code = 403
        return response

    ip = request.remote_addr
    port = request_json.get("port")
    path = request_json.get("path")

    if ip and name and path and port:
        _services[name] = {
            "ip": ip,
            "path": path,
            "port": port
        }

        response.status_code = 201
        return response

    response.status_code = 403
    return response


@app.route("/<string:name>", methods=["DELETE"])
def _unregister(name: str):
    service: dict = _services.get(name)
    request = get_request()
    response = Response()

    if request.remote_addr == service.get("ip"):
        _services.pop("name")
        response.status_code = 204
    else:
        response.status_code = 401

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)
