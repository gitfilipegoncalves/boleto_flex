from flask import Flask

from app import restapi

app = Flask(__name__)
restapi.init_app(app)


@app.route('/')
def hello():
    return 'Hello Flask'
