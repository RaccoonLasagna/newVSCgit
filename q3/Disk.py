import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.color("black")

        t.pendown()
        t.fd(self.dwidth // 2)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth // 2)
        t.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

        t.penup()
        t.goto(self.dxpos, self.dypos)

    def cleardisk(self):
        t.color("white")

        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()
        t.fd(self.dwidth // 2)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth // 2)
        t.penup()

if __name__ == "__main__":
    d = Disk()

    d.showdisk()
    d.cleardisk()

    d.newpos(30, 30)
    d.showdisk()
    d.cleardisk()