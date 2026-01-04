# Mastering NumPy - 1. Working with NumPy Arrays

- [Mastering NumPy - 1. Working with NumPy Arrays](#mastering-numpy---1-working-with-numpy-arrays)
  - [1.0 The Importance of NumPy](#10-the-importance-of-numpy)
  - [1.1 Technical Requirements](#11-technical-requirements)
  - [1.2 Why do we need NumPy?](#12-why-do-we-need-numpy)
  - [1.3 Who uses NumPy?](#13-who-uses-numpy)
  - [1.4 Introduction to Vectors and Matrices](#14-introduction-to-vectors-and-matrices)

## 1.0 The Importance of NumPy

- Theoretical and Practical Information about Vectors and Matrices
- NumPy Array Operations and their Usage in Multi-Dimensional Arrays

## 1.1 Technical Requirements

- Jupyter Notebooks (http://jupyter.org/install)
- Python 3.x
- Anaconda / Miniconda (https://www.anaconda.com/download/)

Within VS Code, "Jupyter" extension (from Microsoft) can be installed

## 1.2 Why do we need NumPy?

NumPy is the most fundamental package for **scientific computing** in Python, and is the base for many other packages.

Following are some well-known libraries which use NumPy features: pyflux, TPOT, xcessiv, xgboost, mlbox, torch, opencv, lightgbm, Keras, gensim, h5py, hyperopt, SciPy, Pandas, Matplotlib, Scikit-Learn

The main work in numerical computing are with **vectors** and **matrices**.

Two key advantages of NumPy from Python are as below:

| Python | NumPy |
| --- | --- |
| Python lists don't support *vectorized* operations. | NumPy supports *vectorized* operations. |
| Python doesn't have fixed type elements in lists and e.g., for loop is not very efficient because, at every iteration, data type needs to be checked. | In NumPy arrays, the data type is fixed. |

## 1.3 Who uses NumPy?

- People who need to work with data and do analysis, modeling, or forecasting

## 1.4 Introduction to Vectors and Matrices

- A `matrix` is a group of numbers or elements which are arranged as a rectangular array.
  - `Square Matrix` refer to the matrix that numbers of rows = numbers of columns
  - `Zero Matrix` (null matrix) refers to a matrix of all 0s, denoted by `0`.
  - `Identity Matrix` refers to a matrix that its diagonal elements are 1 while the others are 0, denoted by `I`
- A `vector` is actually a `matrix` with one row or one column with more than one element.
  - A `vector` can be interpreted as an arrow or direction in an `m` dimensional space.

---

Last updated at: 1/4/2026, 8:51:31 PM 