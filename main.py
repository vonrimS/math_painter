import numpy as np
from PIL import Image

class Canvas:
    """
    Object where all shapes are going to be drawn
    """

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        # create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Convert the current array into an image file"""
        img= Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # changes a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # changes a slice of the array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color




canvas = Canvas(400, 500, (255, 255, 255))
r1 = Rectangle(100, 60, 70, 155, (100, 200, 125))
r1.draw(canvas)
s1 = Square(2, 50, 30, (0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')