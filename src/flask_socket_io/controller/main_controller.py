from flask import render_template

from src.flask_socket_io.domain.flask_socket_io import app


@app.route("/", defaults={})
def main():
    return render_template("index.html")
