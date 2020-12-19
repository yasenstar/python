# Installation of Flask

## using virtual environments

__WHY?__

- Virtual environments are very userful because they prevent package clutter and version conflicts in the system's Python interpreter.
- Creating a virtual environment for each application ensures that applications have access to only the packages that they use, while the global interpreter remains neat and clean and serves only as a source from which more virutal environments can be created.
- As an added benefit, virtual environments don't require administrative rights.

Virtual environments are created with the 3rd-party _virtualenv_ utility.

To check whether you have it installed in your system, use following command:

```
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

```
from flask import Flask
app = Flask(__name__)
```

The only required argument to the __Flask__ class constructor is the name of the main module or package of the application. For most applications, Python's  __\_\_name\_\___ variable is the correct value.

__Note:__ Flask uses the _name_ argument to determine the root path of the application so that it later can find resource files relative to the location of the application.

## Routes and View Functions

Clients such as web browsers send _requests_ to the web server, which in turn sends them to the Flask application instance. The application instance needs to know what code needs to run for each URL requested, so it keeps a mapping of URLs to Python functions. The association between the URL and the function that handles it is called a _route_.

