'''
Define the function DrawDiagonals(txt_input, width, height, png_output) that receives as arguments:
- txt_input: the path to a file containing a list of diagonals to be drawn
- width: width in pixels of the image to be created
- height: height in pixels of the image to be created
- png_output: the path to a PNG image you need to create, containing the diagonals

The function should create a black background image and draw all the diagonals indicated in the 'txt_input' file, in the order they appear in the file.

The txt_file contains, one per line, separated by spaces:
- a word indicating the type of diagonal to be drawn
- the three R G B components of the color to be used
- the coordinates and length of the diagonal
There can be 2 types of diagonal:

- descending diagonal (-45° direction):
    diagonalDOWN R G B x y L
    the diagonal begins at the point (x,y), heads LOW-right, and is L pixels long
    
- ascending diagonal (+45° direction):
    diagonalUP R G B x y L
    the diagonal starts at the point (x,y), heads UP-right, and is L pixels long

Then the function must save the obtained image in the file 'png_output' using the pngmatrix.save_png8 function.
It must also return the number of diagonals drawn of the two types
as a tuple of the two values (DIAGUP, DIAGDOWN).

See the example input and output files in the folder "examples":
  DrawDiagonals("examples/in_1.txt", 256, 512, "examples/out_1.png")
  DrawDiagonals("examples/in_2.txt", 640, 480, "examples/out_2.png")
'''

import pngmatrix


def readDiagonalData(txt_input):
  diagonals = []
  with open(txt_input, 'r', encoding="utf8") as file_ref:
    for line in file_ref:
      diagonals.append(line.split())
  return diagonals


def DrawDiagonals(txt_input, width, height, png_output):
  # your code goes here
  pass


if __name__ == "__main__":
  #DrawDiagonals("examples/in_1.txt", 256, 512, "examples/out_1.png")
  #DrawDiagonals("examples/in_2.txt", 640, 480, "examples/out_2.png")
  print(readDiagonalData("examples/in_1.txt"))
