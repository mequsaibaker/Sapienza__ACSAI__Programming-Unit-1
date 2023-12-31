'''
write 3 recursvive functions to pre-, in-, and post-visit a binary tree, providing the result as a list.
use the provided BinTree class that implements binary trees.
given the following tree:
          a
        /   \
       b     c
      / \   /
     d   e f
        /
       g

pre-visit = ["a", "b", "d", "e", "g", "c", "f"]
in-visit = ["d", "b", "g", "e", "a", "f", "c"]
post-visit = ["d", "g", "e", "b", "f", "c", "a"]
'''


def pre_visit(T):  #(print, left, right)
  # your code goes here
  print(T)
  if T.left != None:
    pre_visit(T.left)
  if T.right != None:
    pre_visit(T.right)
  pass


def in_visit(T):
  # your code goes here
  pass


def post_visit(T):
  # your code goes here
  pass


from bintree import BinTree

if __name__ == "__main__":
  treelist = [
      "a", ["b", ["d", None, None], ["e", ["g", None, None], None]],
      ["c", ["f", None, None], None]
  ]
  tree = BinTree.fromList(treelist)
  # print(tree)
  pre_visit(tree)
