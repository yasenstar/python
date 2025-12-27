from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser type is %s, good day!</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)