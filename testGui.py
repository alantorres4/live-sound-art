from random import *
from tkinter import *
import pyaudio
import numpy as np
from Visual import testFunc

def deleteFunc():
    canvas.delete('all')

def testFunc(barStr):
    stringCount += 1
    if stringCount > 20:
        deleteFunc()
        stringCount -= 5
    if stringCount < 20:
        if len(barStr) > 0:
            x1 = randint(20,430)
            y1 = randint(20,430)
            x2 = randint(20,430)
            y2 = randint(20,430)
            canvas.create_line(x1, y1, x2, y2, fill=f'#{randint(0,0xffffff) :06x}', width=10)
            canvas.update()

global stringCount

window = Tk()
global canvas
canvas = Canvas(window, width=450, height=450, background="white")
canvas.grid(row=0, column=0)

CHUNK = 2**11
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True, frames_per_buffer=CHUNK)

# for i in range(int(10*44100/1024)): #go for a few seconds # CHANGED 10 TO 2
for i in range(20):
    # testFunc("Alan")


    # for i in range(int(10*44100/1024)): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*6
    bars="#"*int(50*peak/2**16)
    testFunc(bars)

window.resizable(0,0)
stream.stop_stream()
stream.close()
p.terminate()
window.mainloop()
