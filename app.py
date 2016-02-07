from flask import Flask
from dbco import db

app = Flask("Ascribe")

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()
