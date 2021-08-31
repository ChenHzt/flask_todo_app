from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

# KuFV0B72s2FofQds

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
