from flask import Flask

app = Flask(__name__)


@app.route("/")
def print_message():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(ssl_context=("server-public-key.pem", "server-private-key.pem"))
