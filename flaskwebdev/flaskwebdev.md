# Installation of Flask

## using virtual environments

__WHY?__

- Virtual environments are very userful because they prevent package clutter and version conflicts in the system's Python interpreter.
- Creating a virtual environment for each application ensures that applications have access to only the packages that they use, while the global interpreter remains neat and clean and serves only as a source from which more virutal environments can be created.
- As an added benefit, virtual environments don't require administrative rights.

Virtual environments are created with the 3rd-party _virtualenv_ utility.

To check whether you have it installed in your system, use following command:

```bash
$ virtualenv --version
```

If doesn't have it yet, install in Linux as below:

```
$ sudo apt install python-virtualenv
```

While, install in Mac OS X with following command:

```
$ sudo easy_install virutalenv
```

After installing, create the Python virtual environment insde the _flasky (your flask working directory)_ folder using the virtualenv command. (The command has a single reuqired argument: the name of the virtual environment). A folder with the chosen name will be created in the current directory and all files associated with the virutal environment will be inside. A commonly used naming convention for virtual environments is to call them _venv_:

```
$ virtualevn venv
created virtual environment CPython3.8.5.final.0-64 in 888ms
  creator CPython3Posix(dest=/Users/yasen/Documents/GitHub/python/flaskwebdev/ch02/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/yasen/Library/Application Support/virtualenv)
    added seed packages: pip==20.3.1, setuptools==51.0.0, wheel==0.36.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

Now you have _venv_ folder inside your working directory with a brand-new virtual environment that contains a private Python interpreter. To start using the virtual environment, you have to "__activate__" it. In Linux bash command line:

```
$ source venv/bin/activate
```

When a virtual environment is activated, the location of its Python interpreter is added to the __PATH__, but his change is not permanent; it affects only your current command session. To remind you that you have activated a virtual environment, the activation command modifies the command prompt to include the name of the environment:

```
(venv) $
```

## Install Flask Python package with pip

To install Flask into the virtual environment, using following command:

```
(venv) $ pip install flask
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 2.9 MB/s 
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 2.4 MB/s 
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 4.9 MB/s 
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp38-cp38-macosx_10_9_x86_64.whl (16 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 64 kB/s 
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, flask
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
WARNING: You are using pip version 20.3.1; however, version 20.3.3 is available.
You should consider upgrading via the '/Users/yasen/Documents/GitHub/python/flaskwebdev/ch02/venv/bin/python -m pip install --upgrade pip' command.
(venv) $
```

# Basic Flask Application Structure

## Flask Application Initialization

All Flask application must create an _application instance_.

The web server passes all requests it receives from clients to this object for handling, using a protocol called __Web Server Gateway Interface (WSGI)__.

The application instances is an object of class __Flask__, usually created as follows:

```python
from flask import Flask
app = Flask(__name__)
```

The only required argument to the __Flask__ class constructor is the name of the main module or package of the application. For most applications, Python's  __\_\_name\_\___ variable is the correct value.

__Note:__ Flask uses the _name_ argument to determine the root path of the application so that it later can find resource files relative to the location of the application.

## Routes and View Functions

Clients such as web browsers send _requests_ to the web server, which in turn sends them to the Flask application instance. The application instance needs to know what code needs to run for each URL requested, so it keeps a mapping of URLs to Python functions. The association between the URL and the function that handles it is called a _route_.

The most convenient way to define a route in a Flask application is through the `app.route` decorator exposed by the application instance, which registers the decorated function as a route. The following example shows how a route is declared using this decorator:

```python
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```

__Note:__ Decorators are a standard feature of the Python; they can modify the behavior of a function in different ways. A common pattern is to use decorators to register functions as handlers for an event.

This sample registers the function `index()` as the handler for the application's root URL. If this application were deployed on a server associated wit the _www.sample.com_ domain name, then navigating to _http://www.sample.com_ on your browser would trigger `index()` to run on the server. The return value of this function, called the _response_, is what the client receives. If the client is a web browser, the response is the document that is displayed to the user.

Function like `index()` are called _view functions_. A response returned by a view function can be a simple string with HTML content, but is can also take more complex forms.

If you pay attention to how some URLs for services that you use every day are formed, you will notice that many have variable sections. For example, the URL for your Facebook profile page is _http://www.facebook.com/<your-name>_, so your username is part of it. Flask supports these type of URLs using a special syntax in the `route` decorator. The following example defines a route that has a dynamic name components:

```python
@app.route('/user/name')
def user(name):
    return '<h1>Hello, $s!</h1> % name
```

The portion enclosed in angle brackets is the dynamic part, so any URLs that match the static portions will be mapped to this route. When the view function is invoked, Flask sends the dynamic component as an argument.

The dynamic components in routes are strings by default but can also be defined with a type. E.g., route `/user/<int:id>` would match only URLs that have an integer in the `id` dynamic segment. Flask supports types `int`, `float`, and `path` for routes. The `path` type also represents a string but does not consider slashes as spearators and instead considers them part of the dynamic component.

## Server Setup

The application instances has a `run` method that launches Flask's integrated development web server:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

The `__name__ == '__main__'` Python idiom is used here to ensure that the development web server is started only when the script is executed directly. When the script is imported by another script, it is assumed that the parent script will launch a different server, so the `app.run()` call is skipped.

Once the servers starts up, it goes into a loop that waits for requests and services them. This loop continues until the application is stopped, for example by hitting `Ctrl-C`.

## A Complete Application

Below is the entire _hello.py_ application script, it's nothing more than the three parts described earlier combined in a single file.

```python
# Example hello.py: a complete Flask application
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>

if __name__ == '__main__":
    app.run(debug=True)
```

