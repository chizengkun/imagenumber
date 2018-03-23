# coding=utf-8

from math import sqrt, cos, sin
from PIL import Image, ImageDraw


class SpireShape(object):
    def __init__(self, draw):
        self.draw = draw
        self.line_width = 1
        self.line_color = (0, 0, 0)
        self.current_point = (0, 0)

    def setPoints(self, points):
        self.points = points

    def setLineWidth(self, line_width):
        self.line_width = line_width

    def setLineColor(self, line_color):
        self.line_color = line_color

    def moveto(self, p):
        self.current_point = p

    def lineto(self, p):
        self.draw.line((self.current_point, p), width=self.line_width, fill=self.line_color)
        self.current_point = p

    def point(self, p):
        self.draw.point(p, fill=self.line_color)
        self.current_point = p

    def spire(self, p, angle, rate):
        '''
        p is start point,angle is start angle,rate is scatter speed len/thita.
            '''
        r = 0;
        thita = 0;
        pi = 3.14
        du = 2 * pi / 360
        while r <= 500.0:
            posX = r * cos(thita + angle * du)
            posY = r * sin(thita + angle * du)

            pSpare = (posX + p[0], posY + p[1])
            self.point(pSpare)

            r = r + thita * rate
            thita = thita + du


# 测试代码
if __name__ == '__main__':
    im = Image.new('RGBA', (1024, 1024), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    b = SpireShape(draw)
    point = (500, 500)
    b.spire(point, 0, 0.2)
    # b.spire(point,90,0.2)

    del draw
    im.show()