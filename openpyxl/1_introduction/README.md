# openpyxl - 1. Introduction

- [openpyxl - 1. Introduction](#openpyxl---1-introduction)
  - [What is `openpyxl`?](#what-is-openpyxl)
  - [Installation and Setup](#installation-and-setup)
  - [Basic Concepts and Terminology](#basic-concepts-and-terminology)

## What is `openpyxl`?

`openpyxl` is a Python library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.

## Installation and Setup

Using `pip` or `pip3`, as below:

```bash
pip install openpyxl
```

This command will download and install the latest stable version of `openpyxl` and its dependencies. You'll need Python 3.7 or higher.

Keep your `pip` in the latest version via `pip intall --upgrade pip` command.

After successful installation, you can verify it by importing the library in a Python interpreter:

```python
import openpyxl
```

If no errors occurs, `openpyxl` is correctly installed.

## Basic Concepts and Terminology

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

---

Last Updated at: 12/27/2025, 3:57:48 PM 