'''
write a function ScanFolder that, given the path to a folder, recursively finds all the files and folders stored in the folder and its subfolders at any level, and returns a tuple. the first item in the tuple is the folder name, the second item is a list containing a string for each file in the folder and a tuple for each subfolder in the folder, stored the same way as the parent folder. files and folder names are alphabetically sorted in all the lists.
for example, given the following folder structure:
a -
  | - t1.txt
  |
  | - b
  |   | - t1.txt
  |   | - t2.txt
  |
  | - c
  |
  | - d
      | - t2.txt

the function ScanFolder("a") returns the list:
("a", [("b", ["t1.txt", "t2.txt"]), ("c", []), ("d", [t2.txt]), "t1.txt"])
'''

# you can only use the following imports:
from os import path, scandir
from os.path import isdir
from os.path import basename


def ScanFolder(folder_path):
  # your code goes here
  result = (basename(folder_path), [])
  obj = scandir(folder_path)
  for item in obj:
    path = folder_path + '/' + item.name
    if not isdir(path):
      result[1].append(item.name)
    else:
      result[1].append(ScanFolder(path))
  return result


if __name__ == "__main__":
  print(ScanFolder("a"))
