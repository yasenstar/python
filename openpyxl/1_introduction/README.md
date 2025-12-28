# openpyxl - 1. Introduction

- [openpyxl - 1. Introduction](#openpyxl---1-introduction)
  - [1.1 What is `openpyxl`?](#11-what-is-openpyxl)
  - [1.2 Installation and Setup](#12-installation-and-setup)
  - [1.3 Basic Concepts and Terminology](#13-basic-concepts-and-terminology)
  - [1.4 First Example: Reading \& Writing a Simple Spreadsheet](#14-first-example-reading--writing-a-simple-spreadsheet)

## 1.1 What is `openpyxl`?

`openpyxl` is a Python library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.

## 1.2 Installation and Setup

Using `pip` or `pip3`, as below:

```bash
pip install openpyxl
```

This command will download and install the latest stable version of `openpyxl` and its dependencies. You'll need Python 3.7 or higher.

```python
pip install openpyxl
Collecting openpyxl
  Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting et-xmlfile (from openpyxl)
  Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-2.0.0 openpyxl-3.1.5
```

Keep your `pip` in the latest version via `pip intall --upgrade pip` command.

After successful installation, you can verify it by importing the library in a Python interpreter:

```python
>>> import openpyxl
```

If no errors occurs, `openpyxl` is correctly installed.

If your installation is not successfully, you may see following error for further troubleshooting:

```python
>>> import openpyxl
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
ModuleNotFoundError: No module named 'openpyxl'
```

## 1.3 Basic Concepts and Terminology

`openpyxl` represents an Excel file as a `workbook`, which contains one or more `worksheets`. A `worksheet` is a grid of `cells` organized into `rows` and `columns`. Each `cell` can contain different data types: numbers, text, formulas, dates, booleans, etc.

Here are the key terminologies:

| Term | Description |
| --- | --- |
| Workbook | The entire Excel file. It's represented by the `workbook` class. |
| Worksheet | A single sheet within the workbook. Represented by the `worksheet` class. |
| Cell | An individual entry in the worksheet, identified by its column and row coordinates (e.g. "A1", "B2"). Accessed using `worksheet["A1"]` or `worksheet.cell(row=1, column=1)`. |
| Row | A horizontal sequence of cells. |
| Column | A vertical sequence of cells. |
| Cell Value | The content of a cell (string, number, formula, etc.) |
| Cell Style | Formatting applied to a cell (font, alignment, number format, etc.) |

## 1.4 First Example: Reading & Writing a Simple Spreadsheet

```python

```

---

Last Updated at: 12/27/2025, 3:57:48 PM 