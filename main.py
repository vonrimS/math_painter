import datetime
import random

from canvas import Canvas
from shapes import Rectangle, Square

# get canvas width and height from the user
width = int(input('Enter canvas width (px): '))
height = int(input('Enter canvas height (px): '))
print(f'...canvas size: {width} x {height}\n')

# make a dictionary of color codes and prompt for color
colors = {'white': (255, 255, 255), 'black': (0,0,0)}
base_canvas_color = input('Choose your canvas base color (white or black): ').lower()
print(f'...canvas base color: {base_canvas_color}\n')

# create a canvas object with user input
canvas = Canvas(height, width, colors[base_canvas_color])

while True:
    shape_type = input('What do you like to draw? (enter \'r\' for rectangle, \'s\' for square, \'q\' for quit): ').lower()
    # ask the user for rectangle data and create rectangle if user entered 'r'
    if shape_type == 'r':
        rec_x = int(input('Enter x of the rectangle: '))
        rec_y = int(input('Enter y of the rectangle: '))
        rec_w = int(input('Enter width of the rectangle: '))
        rec_h = int(input('Enter height of the rectangle: '))
        rec_red = int(input('How much red should the rectangle have: '))
        rec_green = int(input('How much green should the rectangle have: '))
        rec_blue = int(input('How much blue should the rectangle have: '))
        # create the rectangle
        r1 = Rectangle(rec_x, rec_y, rec_w, rec_h, (rec_red, rec_green, rec_blue))
        r1.draw(canvas)
    # ask the user for square data and create square if user entered 's'
    if shape_type == 's':
        sqr_x = int(input('Enter x of the square: '))
        sqr_y = int(input('Enter y of the square: '))
        sqr_s = int(input('Enter side width of the square: '))
        sqr_red = int(input('How much red should the square have: '))
        sqr_green = int(input('How much green should the square have: '))
        sqr_blue = int(input('How much blue should the square have: '))
        # create the square
        s1 = Square(sqr_x, sqr_y, sqr_s, (sqr_red, sqr_green, sqr_blue))
        s1.draw(canvas)

    # randomly fill the canvas
    if shape_type == 'a':
        qnt = int(input('How much geometry figures do you like to put on canvas: '))
        i = 0
        while i < qnt:
            rand_x = random.randrange(width)
            rand_y = random.randrange(height)
            rand_w = random.randrange(width*0.3)
            rand_h = random.randrange(height*0.3)
            rand_red = random.randrange(255)
            rand_green = random.randrange(255)
            rand_blue = random.randrange(255)
            Rectangle(rand_x, rand_y, rand_w, rand_h, (rand_red, rand_green, rand_blue)).draw(canvas)
            i += 1

    # break the loop if user entered 'q' to quit program running
    if shape_type == 'q':
        break

timestamp = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
canvas.make(f'canvas_{timestamp}.png')

