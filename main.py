black = (0,0,0)
white = (255,255,255)

im = [[black]*200 for _ in range(150)]

def draw_h(im, row, color=white):
    width = len(im[0])
    height = len(im)
    if not (0<=row<height):
        return
    for i in range(width):
        im[row][i] = color


def draw_v(im, col, color=white):
    height = len(im)
    width = len(im[0])
    if not (0<=col<width):
        return
    for i in range(height):
        im[i][col] = color

from random import randint

def random_color():
    return randint(0,255), randint(0,255), randint(0,255)
    return tuple(randint(0,255) for _ in 'abc')

def random_lines(im, h_lines, v_lines):
    height, width = len(im), len(im[0])
    if h_lines > height or v_lines > width:
        raise IndexError('Not enough lines or columns in the image')
    done = set()
    for n in range(h_lines):
        line = randint(0, height)
        while line in done:
            line = randint(0, height)
        draw_h(im, line, random_color())
        done.add(line)

    done = set()
    while v_lines > 0:
        col = randint(0, width)
        if col not in done:
            draw_v(im, col, random_color())
            done.add(col)
            v_lines -= 1


# Alternative line for avoiding adjacent lines
# while set(line+i for i in (-1,0,1)).intersection(done):    

# Alternative line for avoiding adjacent vertical lines
# while col not in done and col+1 not in done and col-1 not in done:

# Beware: we should also change the maximum number of lines/cols
# we can draw

def intersections(image):
## Given an image as input, returns the number of pixels that
## are intersections of a vertical line with an horizontal line.
## Assume that the image has a black background    
