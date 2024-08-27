#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get("locale")
     if locale in app.config["LANGUAGE"]:
        print(locale)
        return locale
        
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def get_index_page():
    """render template"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
