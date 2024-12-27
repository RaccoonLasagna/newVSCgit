import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("a")
        self.rabbit=QPixmap("images/rabbit.png")
    
    def paintEvent(self,e):
        p=QPainter()
        p.begin(self)
        p.setPen(QColor(0,143,133))
        p.setBrush(QColor(0,143,133))
        p.drawPolygon([QPoint(70,100),QPoint(100,110),QPoint(130,100),QPoint(100,150),])
        p.drawPie(50,300,100,100,180*16,180*16)
        p.drawPolygon([QPoint(50,350),QPoint(150,350),QPoint(100,150),])
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,0,0))
        p.drawPie(70,350,10,10,180*16,180*32)
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()
def main():
    app=QApplication(sys.argv)
    w=Simple_drawing_window()
    w.show()
    return app.exec()
if __name__=="__main__":
    sys.exit(main())
