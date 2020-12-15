from PyQt5.Qt import QColor
limit = [22, 21]

dirdoc = {83:[0, 1], #아래쪽
          87:[0, -1], #위쪽
          65:[1, -1], #왼쪽
          68:[1, 1]} #오른쪽

map =  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 7, 7, 7, 7, 7, 7, 7, 1, 7, 7, 7, 7, 7, 7, 7, 0, 1],
        [1, 7, 1, 1, 7, 1, 1, 1, 7, 1, 7, 1, 1, 1, 7, 1, 1, 7, 1],
        [1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1],
        [1, 7, 1, 1, 7, 1, 7, 1, 1, 1, 1, 1, 7, 1, 7, 1, 1, 7, 1],
        [1, 7, 7, 7, 7, 1, 7, 7, 7, 1, 7, 7, 7, 1, 7, 7, 7, 7, 1],
        [1, 1, 1, 1, 7, 1, 1, 1, 7, 1, 7, 1, 1, 1, 7, 1, 1, 1, 1],
        [0, 0, 0, 1, 7, 1, 7, 7, 7, 7, 7, 7, 7, 1, 7, 1, 0, 0, 0],
        [1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1],
        [1, 7, 7, 7, 7, 7, 7, 1, 0, 0, 0, 1, 7, 7, 7, 7, 7, 7, 1],
        [1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1],
        [0, 0, 0, 1, 7, 1, 7, 7, 7, 7, 7, 7, 7, 1, 7, 1, 0, 0, 0],
        [1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1],
        [1, 7, 7, 7, 7, 7, 7, 7, 7, 1, 7, 7, 7, 7, 7, 7, 7, 7, 1],
        [1, 7, 1, 1, 7, 1, 1, 1, 7, 1, 7, 1, 1, 1, 7, 1, 1, 7, 1],
        [1, 7, 7, 1, 7, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7, 1, 7, 7, 1],
        [1, 1, 7, 1, 7, 1, 7, 7, 1, 1, 1, 7, 1, 7, 7, 1, 7, 1, 1],
        [1, 7, 7, 7, 7, 1, 7, 7, 7, 1, 7, 7, 1, 7, 7, 7, 7, 7, 1],
        [1, 7, 1, 1, 1, 1, 1, 1, 7, 1, 7, 1, 1, 1, 1, 1, 1, 7, 1],
        [1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

graphic = {1:["■", QColor(0, 0, 255)],  #벽
           9:["pd", QColor(255, 255, 0)],   #플레이어
           0:["＊", QColor(0, 0, 0)],    #빈공간
           2:["◆",QColor(255, 0, 0)],    #고스트1
           7:["＊",QColor(200, 200, 200)], #포인트
           }

pacdir = {83:"▼",
          87:"▲",
          65:"◀",
          68:"▶"}

#벽 번호 1
#플레이어 번호 9
#빈공간 번호 0
#■
#□