'''
Write a function DrawVerticalLine that takes 4 parameters:
- img, an image, defined as a list of lists of tuples (0, 0, 0)
- (x, y),  the coordinates of a point in img
- L, the lingth of a line
The function draws a vertical white line starting from coordinates (x, y) to coordinates (x, y + L - 1).
See the folder "examples" for some example outputs.
'''

import pngmatrix


def DrawVerticalLines(img, x, y, L):
  # your code goes here
  for row in range(y, min(y + L, len(img))):
    img[row][x] = (255, 255, 255)
  pass


if __name__ == "__main__":
  image = [[(0, 0, 0)] * 64 for _ in range(64)]
  DrawVerticalLines(image, 10, 10, 10)
  pngmatrix.save_png8(image, "examples/out1.png")
  image = [[(0, 0, 0)] * 64 for _ in range(64)]
  DrawVerticalLines(image, 50, 0, 45)
  pngmatrix.save_png8(image, "examples/out2.png")
