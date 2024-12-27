import turtle as t
from Disk import Disk

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        # assume turtle is facing up
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        t.fd(self.pthick/2)
        t.lt(90)
        t.fd(self.plength)
        t.lt(90)
        t.fd(self.pthick)
        t.lt(90)
        t.fd(self.plength)
        t.lt(90)
        t.fd(self.pthick/2)
        t.penup()
        pass

    def popdisk(self):
        popped_disk: Disk = self.stack.pop(-1)
        popped_disk.cleardisk()
        popped_disk.newpos(self.pxpos, self.pypos+self.plength+10)
        popped_disk.showdisk()
        return(popped_disk)

    def pushdisk(self, disk: Disk, clearonstart = True):
        if clearonstart:
            disk.cleardisk()
        disk.newpos(self.pxpos, self.pypos+len(self.stack)*20)
        disk.showdisk()
        self.stack.append(disk)

if __name__ == "__main__":
    pole1 = Pole()
    pole1.showpole()
    pole2 = Pole(xpos = 100)
    pole2.showpole()
    pole3 = Pole(xpos = 200)
    pole3.showpole()
    t.done()