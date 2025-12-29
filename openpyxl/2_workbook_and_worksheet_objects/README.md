# openpyxl - 2. Workbook and Worksheet Objects

- [openpyxl - 2. Workbook and Worksheet Objects](#openpyxl---2-workbook-and-worksheet-objects)
  - [2.1 Creating Workbooks](#21-creating-workbooks)
  - [2.2 Accessing Worksheets](#22-accessing-worksheets)
  - [2.3 Creating Worksheets](#23-creating-worksheets)
  - [2.4 Deleting Worksheets](#24-deleting-worksheets)
  - [2.5 Renaming Worksheets](#25-renaming-worksheets)
  - [2.6 Working with Multiple Workbooks](#26-working-with-multiple-workbooks)
  - [2.7 Workbook Properties](#27-workbook-properties)

## 2.1 Creating Workbooks

Use `Workbook()` class constructor to create a new Excel workbook:

```python
```

By default, a new workbook is created with a single, empty worksheet.

You can add more worksheets as needed (using later commands).

Source on `Workbook()`:

```python
def __init__(self,
            write_only=False,
            iso_dates=False,
            ):
  self._sheets = []
  self._pivots = []
  self._active_sheet_index = 0
  self.defined_names = DefinedNameDict()
  self._external_links = []
  self.properties = DocumentProperties()
  self.custom_doc_props = CustomPropertyList()
  self.security = DocumentSecurity()
  self.__write_only = write_only
  self.shared_strings = IndexedList()

  self._setup_styles()

  self.loaded_theme = None
  self.vba_archive = None
  self.is_template = False
  self.code_name = None
  self.epoch = WINDOWS_EPOCH
  self.encoding = "utf-8"
  self.iso_dates = iso_dates

  if not self.write_only:
      self._sheets.append(Worksheet(self))

  self.rels = RelationshipList()
  self.calculation = CalcProperties()
  self.views = [BookView()]
```

## 2.2 Accessing Worksheets

Several methods provide access to worksheets within a workbook.

The most common method is accessing the active worksheet (the one currently selected in Excel), using `workbook.active`.

You can also access worksheets by name or index, see below example:

```python
```

## 2.3 Creating Worksheets

Adding new worksheets is straightforward using the `create_sheet()` method. This method takes the sheet name as the first argument, and optional arguments for `index` (position within the workbook) and `before` (insert before another sheet):

```python
```

## 2.4 Deleting Worksheets

To remove a worksheet, use the `remove()` method:

```python
```

Note: ensure to save the workbook after deleting a sheet.

## 2.5 Renaming Worksheets

Change a worksheet's name using the `title` attribute:

```python
```

## 2.6 Working with Multiple Workbooks

openpyxl allows you to work with multiple workbooks simultaneously.

Just load or create multiple `workbook` objects:

```python
```

## 2.7 Workbook Properties

Below table lists main properties in a `workbook`:

| Property | Description |
| --- | --- |
| `active` | The currently active worksheet. |
| `worksheets` | A list of all worksheets in the workbook. |
| `sheetnames` | A list of the names of all worksheets. |
| `properties` | Access to file properties using the `Workbook.properties` attribute, allowing setting things like author, last modified by, etc. |

Remember to **always** save your changes using `workbook.save("filename.xlsx")` to persist modifications to the Excel file.

Handle potential `FileNotFoundError` exceptions if the specified file doesn't exist when loading a workbook.

Also, it's good practice to close the workbook using `workbook.close()` after you're finished working with it to release resources, though it's automatically handled by Python's garbage collection.

---

Last Updated at: 12/27/2025, 5:52:58 PM 