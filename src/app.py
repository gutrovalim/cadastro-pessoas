from flask import Flask
from src.controller.pessoa import pessoa

app = Flask(__name__)
app.register_blueprint(pessoa)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
