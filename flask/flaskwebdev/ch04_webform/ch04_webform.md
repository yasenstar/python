`request.form` provides access to form data submitted in `POST` requests.

## Install Web Forms extension for Flask

The `Flask-WTF` extension makes working with web forms a much more pleasant experience. This extension is Flask integration wrapper around the framework-agnostic `WTForms` package.

```
(venv) $ pip install flask-wtf
```

## Cross-Site Request Forgery (CSRF) Protection

By default, Flask-WTF protects all forms against Cross-Site Request Forgery (CSRF) attacks. A CSRF attack occurs when a malicious website sends requests to a different website on which the victim is logged in.

To implement CSRF protection, Flask-WTF needs the application to configure an encryption key. Flask-WTF uses this key to generate encrypted tokens that are used to verify the authenticity of requests with form data.

Sample of Flask-WTF configuration:

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

## Form Classes

A simple web foirm that has one test field and a submit button:

```python
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
```

