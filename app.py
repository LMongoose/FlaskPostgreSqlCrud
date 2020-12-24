import os
import flask
import view


# App
_APPNAME = "AnimeListDB"
_IP = "0.0.0.0"
_PORT = os.environ.get("PORT", 5000)
app = flask.Flask(_APPNAME)
app.secret_key = "dattebayo!"

# Routes
view.setDefaultRoutes(app, _APPNAME)
view.setErrorRoutes(app, _APPNAME)


if(__name__ == "__main__"):
	app.run(host=_IP, port=_PORT, debug=True)