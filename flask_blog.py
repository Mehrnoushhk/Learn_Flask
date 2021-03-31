from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Your user agent is {user_agent}</h1>'


@app.route('/user/<name>') 
def hello_world(name):
    return 'Hello, {}!'.format(name)


if __name__ == '__main__':
    app.run(debug=True)