#!/usr/bin/python3
"""Starts a Flask web application.

    The application listens on 0.0.0.0, port 5000.
    Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
        Display a friendly greeting.

        This route displays a simple greeting message when accessed.

        Returns:
            str: A string containing the greeting message.

    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
