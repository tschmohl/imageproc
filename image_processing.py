import pygame as pg
import numpy

# grayPixel: pixel -> pixel
# compute and return a gray pixel with the same intensity
# as the given pixel
def grayPixel(pixel):
    red_intensity = int(pixel[0])
    green_intensity = int(pixel[1])
    blue_intensity = int(pixel[2])
    ave_intensity = (red_intensity + green_intensity+ blue_intensity)//3
    return ((ave_intensity, ave_intensity, ave_intensity))

# channel: pixel -> channel -> pixel
# return a gray pixel with intensity from given channel of given pixel
def channel(pixel,chan):
    return (pixel[chan],pixel[chan],pixel[chan])


# inverse: pixel -> pixel
# return the color negative of the given pixel
def inverse(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])


# intensify: pixel -> nat255 -> pixel
# brighten each channel of pixel by quantity

def intensify(pixel,quantity):
    r = numpy.int32(pixel[0] + quantity)
    g = numpy.int32(pixel[1] + quantity)
    b = numpy.int32(pixel[2] + quantity)
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    return ((numpy.int8(r), numpy.int8(g), numpy.int8(b)))

def deintensify(pixel, quantity):
    r = numpy.int32(pixel[0] - quantity)
    g = numpy.int32(pixel[1] - quantity)
    b = numpy.int32(pixel[2] - quantity)
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    return ((numpy.int8(r), numpy.int8(g), numpy.int8(b)))

def invert(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = inverse(pixels3d[x,y])

def bw(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = grayPixel(pixels3d[x,y])

def lighten(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = intensify(pixels3d[x,y],10)

def darker(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = deintensify(pixels3d[x,y],10)

