# Mastering NumPy - 1. Working with NumPy Arrays

- [Mastering NumPy - 1. Working with NumPy Arrays](#mastering-numpy---1-working-with-numpy-arrays)
  - [1.0 The Importance of NumPy](#10-the-importance-of-numpy)
  - [1.1 Technical Requirements](#11-technical-requirements)
  - [1.2 Why do we need NumPy?](#12-why-do-we-need-numpy)
  - [1.3 Who uses NumPy?](#13-who-uses-numpy)
  - [1.4 Introduction to Vectors and Matrices](#14-introduction-to-vectors-and-matrices)
    - [1.4.1 Matrix Addition and Subtraction](#141-matrix-addition-and-subtraction)
    - [1.4.2 Scalar Multiplication](#142-scalar-multiplication)
    - [1.4.3 Matrix Multiplication](#143-matrix-multiplication)
  - [1.5 Basics of NumPy Array Objects](#15-basics-of-numpy-array-objects)
  - [1.6 NumPy Array Operations](#16-numpy-array-operations)
  - [1.7 Working with Multi-Dimensional Arrays](#17-working-with-multi-dimensional-arrays)
  - [1.8 Indexing, Slicing, ReShaping, Resizing, and BroadCasting](#18-indexing-slicing-reshaping-resizing-and-broadcasting)

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

To display a matrix here in Markdown:

$$\displaystyle
A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

Using syntax:

```
$$\displaystyle
A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$
Note: you may you $$ to put formula center-aligned
```

### 1.4.1 Matrix Addition and Subtraction

$$\displaystyle
\begin{pmatrix}1 & 4 & 7 \\ 2 & 5 & 8\end{pmatrix} +
\begin{pmatrix}10 & 14 & 16 \\ 13 & 18 & 21\end{pmatrix} =
\begin{pmatrix}1+10 & 4+14 & 7+16 \\ 2+13 & 5+18 & 8+21\end{pmatrix} =
\begin{pmatrix}11 & 18 & 23 \\ 15 & 23 & 29\end{pmatrix}
$$

### 1.4.2 Scalar Multiplication

$$\displaystyle
4 \times \begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix} = 
\begin{pmatrix}4 \times 1 & 4 \times 2 \\ 4 \times 3 & 4 \times 4\end{pmatrix} =
\begin{pmatrix}4 & 8 \\ 12 & 16\end{pmatrix}
$$

### 1.4.3 Matrix Multiplication

Imaging there're two matrices as $X$ and $Y$, where $X$ is an $a \times b$ matrix and $Y$ is an $b \times c$ matrix:

$$\displaystyle
X =
\begin{pmatrix}
X_{11} & X_{12} & X_{13} & \ldots & X_{1b} \\
X_{21} & X_{22} & X_{23} & \ldots & X_{2b} \\
X_{31} & X_{32} & X_{33} & \ldots & X_{3b} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
X_{a1} & X_{a2} & X_{a3} & \ldots & X_{ab}
\end{pmatrix}
\hspace{1cm}
Y =
\begin{pmatrix}
Y_{11} & Y_{12} & Y_{13} & \ldots & Y_{1c} \\
Y_{21} & Y_{22} & Y_{23} & \ldots & Y_{2d} \\
Y_{31} & Y_{32} & Y_{33} & \ldots & Y_{3d} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
Y_{b1} & Y_{b2} & Y_{b3} & \ldots & Y_{bc}
\end{pmatrix}
$$

The product of these two matrices will be as follows:

```math
Z = \begin{pmatrix}
z_{11} & z_{12} & z_{13} & \ldots & z_{1c} \\
z_{21} & z_{22} & z_{23} & \ldots & z_{2c} \\
z_{31} & z_{32} & z_{33} & \ldots & z_{3c} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
z_{a1} & z_{a2} & z_{a3} & \ldots & z_{ac} \end{pmatrix}
```

So each element of the product matrix is calculated as follows:

$$
Z_{ij} = x_{i1}y_{1j} + \ldots + x_{ib}y_{bj} = \sum_{k=1}^{b} x_{ib}y_{bj}
$$

For matrix product sample:

```math
Z_{22} = X_{23} \times Y_{32} =
\begin{pmatrix} 1 & 0 & 4 \\ 3 & 3 & 1 \end{pmatrix}
\times
\begin{pmatrix} 2 & 5 \\ 1 & 1 \\ 3 & 2 \end{pmatrix}
= \\
\begin{pmatrix} (1\times2)+(0\times1)+(4\times3) & (1\times5)+(0\times1)+(4\times2) \\ (3\times2)+(3\times1)+(1\times3) & (3\times5)+(3\times1)+(1\times2) \end{pmatrix}
=
\begin{pmatrix} 14 & 13 \\ 12 & 20 \end{pmatrix}
```

Verify in NumPy:

```python
import numpy as np
x = np.array([
    [1, 0, 4],
    [3, 3, 1]
])
y = np.array([
    [2, 5],
    [1, 1],
    [3, 2]
])
print(x.dot(y))
```

## 1.5 Basics of NumPy Array Objects

What makes NumPy special is the usage of multi-dimentional arrays called `ndarrays`.

## 1.6 NumPy Array Operations

This section covers creation and manipulation of numerical data with NumPy.

## 1.7 Working with Multi-Dimensional Arrays

Stacking: merge two arrays
- `hstack`: is used for stakcing arrays horizontally (column-wise)
- `vstack`: is used for stacking arrays vertically (row-wise)

## 1.8 Indexing, Slicing, ReShaping, Resizing, and BroadCasting

---

Last updated at: 1/6/2026, 11:37:09 AM  
