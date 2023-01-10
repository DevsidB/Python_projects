import os

file1 = "to delete.txt"
file2= "renamed_by_python.txt"

with open (file1) as f:
    content= f.read()

with open (file2, 'w') as f:
    f.write(content)

os.remove(file1)

