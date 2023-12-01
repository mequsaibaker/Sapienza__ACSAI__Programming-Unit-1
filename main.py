# tasks:

# 1. write a function that loads the image "Mario.png" (the filename is a
# parameter) and returns it as a list of lists
# (use the function pngmatrix.load_png8)

# 2. turn Mario into Luigi: write a function that takes Mario as a parameter
# and turns his trousers form red (227, 6, 19) to blue (0, 191, 99)
# (Luigi is copied from Mario before making any change);
# the function returns Luigi as a list of lists

# 3. mirror Luigi: write a function that receives Luigi as a parameter and
# mirrors him in-place; the function does not return anything

# 4. write a function that receives Mario and Luigi as parameters and
# creates a new image by gluing them together and returns the resulting image

# 5. write a function that takes Mario, Luigi and a background image filename
# as parameters, draws Mario and Luigi on the background image at position
# (96, 146) (Mario) and (154, 96) (Luigi), and returns and saves the resulting image

# 6. rotate Luigi: write a function that takes Luigi as a parameter and rotates
# him by 90 degree clockwise in-place (the function does not return anything)

import pngmatrix


def f1_LoadMario(filename: str) -> list:
  img = pngmatrix.load_png8(filename)
  return img


def f2_ComputeLuigi(Mario: list) -> list:
  Luigi = []
  for row in Mario:
    Luigi.append(row.copy())

  for y in range(len(Luigi)):
    for x in range(len(Luigi[y])):
      if Luigi[y][x] == (227, 6, 19):
        Luigi[y][x] = (0, 191, 99)
  return Luigi


def f3_MirrorLuigi(Luigi: list) -> None:
  half_index = len(Luigi[0]) // 2
  for y in range(len(Luigi)):
    for x in range(half_index):
      first_x = x
      second_x = len(Luigi[0]) - 1 - x
      temp = Luigi[y][first_x]
      Luigi[y][first_x] = Luigi[y][second_x]
      Luigi[y][second_x] = temp
  pass


def f4_GlueMarioAndLuigi(Mario: list, Luigi: list) -> list:
  final_img = []
  for y in range(len(Mario)):
    final_img.append(Mario[y] + Luigi[y])
  return final_img


def f5_DrawMarioAndLuigi(Mario: list, Luigi: list, bg_filename: str) -> list:
  start_x_Mario = 96
  start_y_Mario = 146
  start_x_Luigi = 154
  start_y_Luigi = 96
  bg_img = pngmatrix.load_png8(bg_filename)
  for y in range(len(Mario)):
    for x in range(len(Mario[y])):
      bg_img[start_y_Mario + y][start_x_Mario + x] = Mario[y][x]
  for y in range(len(Luigi)):
    for x in range(len(Luigi[y])):
      bg_img[start_y_Luigi + y][start_x_Luigi + x] = Luigi[y][x]

  pngmatrix.save_png8(bg_img, 'background_new.png')
  return bg_img


def f6_RotateLuigi(Luigi: list) -> None:
  Luigi_rotated = []
  for x in range(len(Luigi[0])):
    temp_row = []
    for y in range(len(Luigi)):
      temp_row.append(Luigi[y][x])
    Luigi_rotated.append(temp_row[::-1])
  Luigi.clear()
  for row in Luigi_rotated:
    Luigi.append(row)
  pass


if __name__ == "__main__":
  M = f1_LoadMario("Mario.png")
  print(M)
  L = f2_ComputeLuigi(M)
  f3_MirrorLuigi(L)
  pngmatrix.save_png8(L, "Luigi_mirrored.png")
  M2 = f4_GlueMarioAndLuigi(M, L)
  pngmatrix.save_png8(M2, "MarioLuigi_glued.png")
  f5_DrawMarioAndLuigi(M, L, "background.png")
  f6_RotateLuigi(L)
  pngmatrix.save_png8(L, "Luigi_rotated.png")
