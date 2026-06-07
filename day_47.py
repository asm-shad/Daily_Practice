from flask import Flask

app = Flask(__name__)

def hello_world():
    return "Hello guys what are u gonna do in Wednesday!"

if __name__ == '__main__':
    app.run(debug=True)