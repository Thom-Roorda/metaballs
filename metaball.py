import pygame as pg

class MetaBall():
    
    def __init__(self, x, y, dx, dy, r):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r


    def update(self, PG_WINDOW):

        WINDOW_WIDTH = PG_WINDOW.get_width()
        WINDOW_HEIGHT = PG_WINDOW.get_height()

        if self.x - self.r < 0 or self.x + self.r > WINDOW_WIDTH:
            self.dx *= -1
        if self.y - self.r < 0 or self.y + self.r > WINDOW_HEIGHT:
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy


    def draw(self, PG_WINDOW):
        pg.draw.circle(PG_WINDOW, (255, 255, 255), (self.x, self.y), self.r)