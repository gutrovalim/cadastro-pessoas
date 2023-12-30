from flask import Flask
from controller.pessoa import pessoa
from controller.email import email

app = Flask(__name__)
app.register_blueprint(pessoa)
app.register_blueprint(email)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
