'''
write a function LongestLine that is provided as input the path to a grayscale image; the function finds all the horizontal gray lines in the image (the image background is black) and returns the length of the longest line.
each row of the image can contain one line max.
the function calls another function FindLineStartEnd that receives as input a single row of the image and recursively searches for a line, returning a tuple (start, end) with the start and end coordinates of the line, if found; it returns (None, None), otherwise.

'''

import pngmatrix


def FindLineStartEnd(single_row):
  # your code goes here
  if single_row == []:
    return -1, -1, False, False
  else:
    x_start, x_end, start_flag, end_flag = FindLineStartEnd(single_row[1:])
    if not end_flag:
      if single_row[0] != (0, 0, 0):
        end_flag = True
      return x_start - 1, x_end - 1, start_flag, end_flag
    else:
      if not start_flag:
        if single_row[0] == (0, 0, 0) and single_row[1] != (0, 0, 0):
          start_flag = True
        return x_start - 1, x_end, start_flag, end_flag
      else:
        return x_start, x_end, start_flag, end_flag


def LongestLine(path_to_a_gray_image):
  # your code goes here
  max_len = 0
  img = pngmatrix.load_png8(path_to_a_gray_image)
  for row in img:
    x_start, x_end, start_flag, end_flag = FindLineStartEnd(row)
    max_len = max(max_len, x_end - x_start)
  return max_len


if __name__ == "__main__":
  print(LongestLine("a grayscale image.png"))
