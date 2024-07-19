# write a function that receives a folder name as parameter and returns a
# tree with all of its subfolders, in which each node contains the path
# of the corresponding subfolder

# you have to use the provided NTree class in the ntree.py file
# to manage the file structure as a n-ary tree

# you can use os.listdir to get the list of all the files and subfolders
# for a given folder and os.path.isdir to know whether a given path is a folder

import os

from ntree import NTree


def SubFoldersTree(folder_name: str) -> NTree:
  node = NTree(folder_name)
  items = os.listdir(folder_name)
  for item in items:
    if os.path.isdir(folder_name + "/" + item):
      node.children.append(SubFoldersTree(folder_name + "/" + item))
  return node


if __name__ == "__main__":
  print(SubFoldersTree("testfolder"))
