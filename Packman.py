import sys
import time
from Engine import dirdoc, maploader
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QColor, QTextCursor
from Data import map, graphic, pacdir


class Pacman(QWidget):

    global summon
    summon = 2
    global MAP
    MAP = maploader()
    global clock
    clock = 0

    def __init__(self):
        super().__init__()
        self.setStyleSheet("margin: 10px; padding: 10px; \
                            background-color: \
                            rgba(255,255,0,0); ")

        self.screen = QTextEdit()
        self.screen.setReadOnly(True)
        self.screen.setFont(QFont("Bitstream Vera Sans Mono",20))

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.screen, 0, 0, 1, 2)

        self.score = QLabel()
        grid.addWidget(self.score, 1, 0)
        self.score.setFont(QFont("Bitstream Vera Sans Mono",20))
        self.score.setStyleSheet("color:white; background-color:black; border-color:blue;border-width: 2px;border-style: outset;")
        self.score.setText(str(MAP.playbody.point))

        self.startbutton = QPushButton()
        grid.addWidget(self.startbutton, 1, 1)
        self.startbutton.setFont(QFont("Bitstream Vera Sans Mono",20))
        self.startbutton.setStyleSheet("color:white; background-color:black; border-color:blue;border-width: 2px;border-style: outset;")
        self.startbutton.setText("START")
        self.startbutton.clicked.connect(self.gamestart)

        MAP.mapupdate()
        self.mapupdate()

        #182
        self.setWindowTitle('PAC-MAN')
        self.move(350, 100)
        self.resize(700, 800)
        self.show()



    def keyPressEvent(self, e):
        global summon
        end = QMessageBox()
        try:
            if MAP.playbody.point == 60 and summon ==2:
                MAP.goastsec()
                summon -= 1
            if MAP.playbody.point == 120 and summon ==1:
                MAP.goastthi()
                summon -= 1
            if MAP.playbody.point >= 181:
                MAP.playable = False
                self.setStyleSheet("margin: 10px; padding: 10px; \
                                            background-color: \
                                            rgba(255,255,255,255); ")
                end.about(self, "", "Game Clear!")
            elif MAP.playbody.location == MAP.goast1.location:
                MAP.playable = False
                self.setStyleSheet("margin: 10px; padding: 10px; \
                                            background-color: \
                                            rgba(255,255,255,255); ")
                end.about(self, "", "Game Over!")
            else:
                if e.key() in dirdoc.keys() and MAP.playable == True:
                    MAP.update(e.key())
                    self.mapupdate()
                    self.score.setText(str(MAP.playbody.point))
        except:
            print("keyPressEvent error")

    def mapupdate(self):
        self.screen.setText("")
        for i in map:
            for j in i:
                self.screen.setTextColor(graphic[j][1])
                if graphic[j][0] == "pd":
                    self.screen.insertPlainText(pacdir[MAP.playbody.direction])
                else:
                    self.screen.insertPlainText(graphic[j][0])
            if i != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]:
                self.screen.insertPlainText("\n")

    def gamestart(self):
        MAP.playable = True

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Pacman()
   sys.exit(app.exec_())