from random import *
from tkinter import *

def testFunc(barStr):
    # print(barStr)
    # if len(barStr) == 0:
    #     print("zz")
    # else: 
    #     if len(barStr) < 15:
    #         print("normal")
    #     else:
    #         if len(barStr) < 2:
    #             print("louder")
    #         else:
    #             if len(barStr) < 40:
    #                 print("cough")
    #             else:
    #                 if len(barStr) < 60:
    #                     print("TOO LOUD")
    if len(barStr) > 0:
        x1 = randint(0,400)
        y1 = randint(0,400)
        x2 = randint(0,400)
        y2 = randint(0,400)
        canvas.create_line(x1, y1, x2, y2, fill=f'#{randint(0,0xffffff) :06x}', width=20)


