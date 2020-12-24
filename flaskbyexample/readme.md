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

