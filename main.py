'''
write a function ScanFolder that, given the path to a folder, recursively finds all the files and folders stored in the folder and its subfolders at any level, and returns their paths as a list of strings, sorted alphabetically.
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
["a", "a/b", "a/b/t1.txt", "a/b/t2.txt", "a/c", "a/d", "a/d/t2.txt", "a/t1.txt"]
'''

# you can only use the following imports:
from os import scandir
from os.path import isdir


def ScanFolder(folder_path):
  # your code goes here
  result = [folder_path]
  obj = scandir(folder_path)
  for item in obj:
    path = folder_path + '/' + item.name
    if not isdir(path):
      result.append(path)
    else:
      result += ScanFolder(path)
  result.sort()
  return result


if __name__ == "__main__":
  # ScanFolder("a")
  print(ScanFolder("a"))
  # print([i.name for i in scandir("a")])
