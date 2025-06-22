# Chapter 2: Hello, Python

Programs are made up of commands that tell the computer what to do. There commands are called _statements_, which the computer executes.

## 2.1 How Does a Computer Run a Python Program?

There are 2 ways to use the Python interpreter:

1. to tell is to execute a Python program that is saved in a file with a .py extension
2. to interact with it in a program called a _shell_, where you type statements one at a time.

## 2.2 Expressions and Values: Arithmetic in Python

Like any programming language, Python can _evaluate_ basic mathematical expressions, for example below:

```python
>>> 4 + 13
17
>>> 15 - 3
12
>>> 4 * 7
28
>>> 5 / 2
2.5
>>> 4 / 2
2.0
```

### Types

An expression involving two `floats` produces a `float`:

```python
>>> 17.0 - 10.0
7.0
```

When an expression's operands are an `int` and a `float`, Python automatically converts the `int` to a `float`. This is why the following two expressions both return the same answer:

```python
>>> 17.0 - 10
7.0
>>> 17 - 10.0
7.0
```

You can omit the zero after the decimal point when writing a floating-point number:

```python
>>> 17 - 10.
7.0
>>> 17. - 10
7.0
```

### Integer Division, Modulo, and Exponentiation

