import requests
from flask import Flask

PORT = 7777
CONTENT_PATH = "/content"
SERVICE_NAME = "test"
REGISTER_URL = "http://localhost:8080/"


def register():
    request = {
        "port": PORT,
        "path": CONTENT_PATH
    }

    for _ in range(5):
        try:
            print("Registering service... ", end="")
            response = requests.post(REGISTER_URL + SERVICE_NAME, json=request)

            if not (200 <= response.status_code < 300):
                response.raise_for_status()

            print("Success!")
            break
        except Exception as ex:
            print("Error", ex)


def unregister():
    try:
        print("Unregistering service... ")
        response = requests.delete(REGISTER_URL + SERVICE_NAME)

        if not (200 <= response.status_code < 300):
            response.raise_for_status()

        print("Success!")
    except Exception as ex:
        print("Error", ex)


app = Flask(__name__)


@app.route(CONTENT_PATH, methods=["GET"])
def _content():
    return "Hello World"


if __name__ == "__main__":
    register()
    app.run(host="0.0.0.0", port=PORT)
    unregister()
