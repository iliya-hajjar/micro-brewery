from flask import Flask, request
from utils import validate, access

server = Flask(__name__)


@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err


if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0")
