'''
write a function LongestLine that is provided as input the path to a grayscale image; the function finds all the horizontal gray lines in the image (the image background is black) and returns the length of the longest line.
each row of the image can contain one line max.
the function calls another function FindLineStartEnd that receives as input a single row of the image and recursively searches for a line, returning a tuple (start, end) with the start and end coordinates of the line, if found; it returns (None, None), otherwise.

'''

import pngmatrix


def FindLineStartEnd(single_row):
  # your code goes here
  pass


def LongestLine(path_to_a_gray_image):
  # your code goes here
  pass


if __name__ == "__main__":
  LongestLine("a grayscale image.png")
