## Error of importing Flask Boostrap

Error message:

```python
% python app.py
Traceback (most recent call last):
  File "app.py", line 2, in <module>
    from flask import Flask, render_template
ImportError: No module named flask
(base) yasen@YasendeMacBook-Pro ch03.3 % python3 app.py
Traceback (most recent call last):
  File "/Users/yasen/Documents/GitHub/python/flaskwebdev/ch03.3/app.py", line 2, in <module>
    from flask import Flask, render_template
ModuleNotFoundError: No module named 'flask'
```

Checking from web, found since Flask 0.11, importing extention with `flask.ext` is deprecated

Now should use: `from flask_boostrap import Boostrap`

## Flask-Boostrap Usage

URL: [bootstrap-flask basic usage](https://bootstrap-flask.readthedocs.io/en/stable/basic.html)

Installation:

```
$ pip install bootstrap-flask
```

This project cannot work with Flask-Boostrap at the same time. If you have already installed Flask-Boostrap in the sam Python environment, you have to uninstall it and then reinstall this project:

```
$ pip uninstall flask-bootstrap bootstrap-flask
$ pip install bootstrap-flask
```

Initialization:

```python
from flask-bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap(app)
```
