# write a function that receives an image and an integer value as a parameter,
# and draws a red circle centered in the center of the image
# (the function does not return anything!)

import math
import pngmatrix

def findDistance(x1,y1,x2,y2):
  dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return dis

def isInsideCircle(dis, radius):
  return dis <= radius

def findCenter(img):
  y = len(img) // 2
  x = len(img[0]) // 2
  return x, y

def DrawCircle(image : list, radius : int):
  red = (255, 0, 0)
  x1, y1 = findCenter(image)
  for y2 in image:
    for x2 in image[y2]:
      dis = findDistance(x1,y1,x2,y2)
      if isInsideCircle(dis, radius):
        image[y2][x2] = red
  pass


if __name__ == "__main__":
  I = [[(0, 0, 0)] * 100 for x in range(100)]
  DrawCircle(I, 25)
  pngmatrix.save_png8(I, "result.png")