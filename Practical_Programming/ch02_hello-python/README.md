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

If we want only the integer part of a division result, e.g. to know how many 24-hour days there are in 53 hours, use _integer division_: (note: Python doesn't round the result of integer division, instead, it takes the _floor_ of the result which means it's the round down)

```python
>>> 53 // 24
2
>>> 17 // 10
1
>>> -17 // 10
-2
>>> 17 // -10
-2
```

To find out how many hours are left over using the _modulo_ operator:

```python
>>> 53 % 24
5
>>> 17 % 10
7
>>> -17 % 10
3
>>> 17 % -10
-3
```

Floating-point numbers can be operands for `//` and `%` as well:

```python
>>> 3.3 // 1
3.0
>>> 3 // 1.0
3.0
>>> 3 // 1.1
2.0
>>> 3.5 // 1.1
3.0
>>> 3.5 // 1.3
2.0

>>> 3.3 % 1
0.2999999999999998
>>> 3 % 1.0
0.0
>>> 3 % 1.1
0.7999999999999998
>>> 3.5 % 1.1
0.19999999999999973
>>> 3.5 % 1.3
0.8999999999999999
```

`Power` operand:

```python
>>> 3 ** 6
729
>>> 4 ** 0.5
2.0
```

## 2.3 What _is_ a Type?

In computing, a Type consists of two things:

- a set of values, and
- a set of operations that can be applied to those values

## 2.4 Variables and Computer Memore: Remembering Values

A name that refers to a value is called a _variable_.

Variables are called _variables_ because their values can vary as the program executes.