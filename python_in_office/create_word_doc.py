import os
from docx import Document

work_path = os.getcwd()

dir_name = "python_in_office"

file_name = "test.docx"

target_dir = os.path.join(work_path, dir_name)
print(target_dir)

full_path = os.path.join(work_path, dir_name, file_name)
print(full_path)

doc = Document()

doc.save(full_path)