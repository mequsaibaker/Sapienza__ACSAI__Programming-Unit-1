'''
write a function LongestLine that is provided as input the path to a grayscale image; the function finds all the horizontal gray lines in the image (the image background is black) and returns the length of the longest line.
each row of the image can contain one line max.
the function calls another function FindLineStartEnd that receives as input a single row of the image and recursively searches for a line, returning a tuple (start, end) with the start and end coordinates of the line, if found; it returns (None, None), otherwise.

'''

import pngmatrix


def FindLineStartEnd(single_row):
  # your code goes here
  start = None
  end = None
  if end != None or len(single_row) == 0:
    return None, None
  else:
    if single_row[0] != (0, 0, 0):
      end = FindLineStartEnd(single_row[1:])
      if start is None:
        start = single_row[0]
      return end + 1
  pass


def LongestLine(path_to_a_gray_image):
  # your code goes here
  max_len = 0
  img = pngmatrix.load_png8(path_to_a_gray_image)
  for row in img:
    start, end = FindLineStartEnd(row)
    max_len = max(max_len, end - start)
  return max_len


if __name__ == "__main__":
  LongestLine("a grayscale image.png")
