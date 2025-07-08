from flask import Flask

app = Flask(__name__)

from classificacao.routes import home
