# Flask by Example

Unleash the full potential of the Flask web framework by creating simple yet powerful web applications

Author: Gareth Dwyer

_In theory, nothing works, but everyone knows why._

_In practice, everything works but no one knows why._

_Here, we combine theory and practice; nothing works and no one knows why!_

## Chaptr 1: Hello World!

Definition: Flask is a micro framework for Python web development. (A framework, in the simplest terms, is a library or collection of libraries that aims to solve a part of generic problem instead of a complete specific one.)

When building web applications, there're some problems that will always need to be solved, such as

- Routing from URLs to resources
- Inserting dynamic data in HTML, and
- Interacting with an end user

__Flask__ is a micro framework because it implements ony core functionality (including routing) but leaves more advanced functionality (including authentication and database ORMs) to extensions. The result of this is less initial setup for the _first-time user_ and more choice and flexibility for the _experienced user_. This is in contrast with "fuller" frameworkds, such as __Django__, which dictate their own ORM and authentication technologies.

### Creating Flask Development Environment

Installing Flask

```
pip install --user flask
```

### HelloWorld.py

```python
from flask import Flask     # imports Flask from the package flask

app = Flask(__name__)       # create an instance of the Flask object using module's name as a parameter

@app.route("/")     # Python decorator.
# this URL routing decorator means that the function directly below it should be called wheneven a user visits the main root page of web application (which is defined by the single forward slash).

def index():
    return "Hello World! (Flask By Example)"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
# a Python idiom with simple conditional statement that evaluates to True if our application is run directly.
```

Run the code via `python helloworld.py`, with following output in Terminal:

```
 * Serving Flask app "helloworld" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 644-002-446
127.0.0.1 - - [24/Dec/2020 12:55:34] "GET / HTTP/1.1" 200 -
```

The last line is when visiting from web browser, will have new line when refresh the webpage.

