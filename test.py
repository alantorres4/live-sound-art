import pyaudio
import numpy as np
# from Visual import testFunc
from random import *
from tkinter import *

def random_color():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    color_code = '#'
    for i in range(0,6):
        color_code = color_code + choice(hex_chars)
    return color_code

window = Tk()
canvas = Canvas(window, width=400, height=400, background='#99ba86')
canvas.grid(row=0, column=0)

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)

# for i in range(int(10*44100/1024)): #go for a few seconds
for i in range(0,100):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*6
    bars="#"*int(50*peak/2**16)
    # visualObj = Visual(bars)
    # testFunc(bars)
    x1 = randint(0,400)
    y1 = randint(0,400)
    x2 = randint(0,400)
    y2 = randint(0,400)
    random_width = randint(1,20)
    canvas.create_line(x1,y1,x2,y2,fill=random_color(), width=random_width)
    canvas.update()

stream.stop_stream()
stream.close()
p.terminate()

window.mainloop()
