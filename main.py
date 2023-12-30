# A function that randomly draws n squares of a random color in the
# image. Squares are empty

from random import randint
import pngmatrix


def random_color():
  return randint(0, 255), randint(0, 255), randint(0, 255)


def draw_square(im, r, c, side):
  color = random_color()
  for y in range(c, c + side):
    im[r][y] = color
    im[r + side - 1][y] = color
  for x in range(r, r + side):
    im[x][c] = color
    im[x][c + side - 1] = color


def draw_random_squares(im, n):
  w, h = len(im[0]), len(im)
  while n > 0:
    r, c = randint(0, h - 1), randint(0, w - 1)
    side = randint(1, min(h - r, w - c))
    draw_square(im, r, c, side)
    n -= 1


# A function that gets an image as input, a pixel (r, c) and a color
# c and colors with color all the black pixels adjacent to (r,c) and
# to any of its adjacent pixel image. The function should have a
# behaviour similar to the "Fill bucket" of paint.


def fill_bucket(im, row, col, color):
  pass


if __name__ == '__main__':
  img = [[(0, 0, 0)] * 120 for _ in range(120)]
  draw_random_squares(img, 20)
  pngmatrix.save_png8(img, 'out1.png')
