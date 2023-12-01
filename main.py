'''
write a function that is provided as input the path to a grayscale image; the function finds all the horizontal gray lines in the image (the image background is black) and returns a list of tuples (color, length) for each line found in the image, in which "color" is the (R, G, B) tuple representing the color of a line and "length" is the corresponding length; tuples must be sorted from the longest line to the shortest one, and, if several lines have the same length, by color intensity, from the brightest to the darkest.
'''

import pngmatrix


def LongestLine(path_to_a_gray_image):
  # your code goes here
  img = pngmatrix.load_png8(path_to_a_gray_image)

  len_list = []
  for y in range(len(img)):
    row_ind = 0
    while row_ind < len(img[y]) - 1:
      cur_rbg = img[y][row_ind]
      line_len = 1
      while cur_rbg != (0, 0, 0) and cur_rbg == img[y][row_ind + 1]:
        line_len += 1
        row_ind += 1
      if line_len > 1:
        len_list.append((cur_rbg, line_len))
      row_ind += 1
  return len_list


if __name__ == "__main__":
  LongestLine("a grayscale image.png")
