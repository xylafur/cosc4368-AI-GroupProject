import pygame
import numpy

def __init__(self):
    pygame.init()

# Holds class information for the display window as well as methods to create the initial visualization of the world
class Display():
    def __init__(self):
        pygame.init()

        self.WINDOW_HEIGHT = 800
        self.WINDOW_WIDTH = 800
        self.OFFSET = 2
        self.display = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 20)
        self.squares = []
        self.labels = []

# Create_World(TitleOfExperiment, HeightOfGameWorld, WidthOfGameWorld)
# Title: Possibly name of policy?
# Height/Width: Number of blocks

# Some of this may seem convoluted but obtaining consistency in the margins and shapes proved difficult, thus the
# constants and frivolous calculations
# For every cell in the grid, a square is created, which holds a list of Triangle objects, which in turn holds the
# coordinates of the three vertices of a triangle

    def Create_World(self, title, height, width):
        pygame.display.set_caption(title)
        self.display.fill(Colors.black)

        margin = self.WINDOW_HEIGHT * .1
        blockSize = (self.WINDOW_HEIGHT - margin * 2) / height - self.OFFSET * 1.75

        #draw grid
        grid = pygame.Rect(margin, margin, self.WINDOW_WIDTH - margin * 2, self.WINDOW_HEIGHT - margin * 2)
        pygame.draw.rect(self.display, Colors.white, grid)

        for y in range(height):
            for x in range(width):
                x_val = x * (blockSize + 3) + margin + self.OFFSET
                y_val = y * (blockSize + 3) + margin + self.OFFSET
                square = Square(x_val, y_val, blockSize)
                self.squares.append(square)

        for i in range(len(self.squares)):
            pygame.draw.rect(self.display, Colors.white, self.squares[i].shape)
            for triangle in self.squares[i].triangles:
                pygame.draw.polygon(self.display, Colors.green, [triangle.v1, triangle.v2, triangle.v3], 0)

                # Text is not behaving as nicely as I would have hoped
                text = self.font.render('-.--', True, Colors.black)
                textRect = text.get_rect()
                textRect.center = triangle.get_center()
                self.display.blit(text, triangle.get_center())
                self.labels.append(text)





        pygame.display.update()

# Each square will have associated with it 4 triangle objects, each of which holds 3 number pairs representing the vertices
# of a triangle, which can be later used to access them individually and update color/value simply through future methods
class Square():
    def __init__(self, x, y, size):
        self.OFFSET = 2

        self.shape = pygame.Rect(x, y, size, size)

        self.triangles = []
        #LEFT
        self.triangles.append(Triangle(tuple(numpy.add(self.shape.topleft, (0, self.OFFSET))),
                                       tuple(numpy.add(self.shape.center, (-self.OFFSET, 0))),
                                       tuple(numpy.add(self.shape.bottomleft, (0, -self.OFFSET)))))
        #TOP
        self.triangles.append(Triangle(tuple(numpy.add(self.shape.topleft, (self.OFFSET,0))),
                                       tuple(numpy.add(self.shape.center, (0,-self.OFFSET))),
                                       tuple(numpy.add(self.shape.topright, (-self.OFFSET, 0)))))
        #RIGHT
        self.triangles.append(Triangle(tuple(numpy.add(self.shape.topright,(0, self.OFFSET))),
                                       tuple(numpy.add(self.shape.center,(self.OFFSET,0))),
                                       tuple(numpy.add(self.shape.bottomright,(0,-self.OFFSET)))))
        #BOTTOM
        self.triangles.append(Triangle(tuple(numpy.add(self.shape.bottomleft, (self.OFFSET,0))),
                                       tuple(numpy.add(self.shape.center, (0,self.OFFSET))),
                                       tuple(numpy.add(self.shape.bottomright, (-self.OFFSET,0)))))

class Triangle():
    def __init__(self, p1, p2, p3):
        self.v1 = p1
        self.v2 = p2
        self.v3 = p3

# Returns the centroid of the Triangle. Aim was to use this to center the rectangle object associated with the text label
    def get_center(self):
        Ox = (self.v1[0] + self.v2[0] + self.v3[0]) / 3
        Oy = (self.v1[1] + self.v2[1] + self.v3[1]) / 3
        return (Ox, Oy)


class Colors():
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,128,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    grey = (128,128,128)

# Use matplotlib to output q table to graph? ( 25 states)

def main():
    d = Display()
    d.Create_World('Greedy Policy', 5, 5)

main()