import serial
import serial.tools.list_ports
import matplotlib; matplotlib.use("TkAgg") # Don't know what this line is, but it is NECESSARY FOR ANIMATE TO WORK!!!
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math
import random


portlist = list(serial.tools.list_ports.comports())
print('Connecting to serial...')
print('Available serial ports:')
for item in portlist:
    print(item[0])

# configure the serial port
print('Opening port COM3 [USB]')
ser = serial.Serial(
    port='COM3',
    # port=item[0],
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()
print('COM3 [USB] successfully connected.')

# ================================================================
xsize = 100


def my_func():
    t = data_gen.t
    lastTemp = 22
    while 1:
        t+=1
        strin = ser.readline()
        strinDecoded = strin.decode()
        tempString = strinDecoded[:2]
        tempVal = int(tempString)
        if (tempVal < lastTemp - 3):
            tempVal = lastTemp
        else:
            lastTemp = tempVal
        if (tempVal > lastTemp + 3):
            tempVal = lastTemp
        else:
            lastTemp = tempVal
        print(tempVal)
        #yield t, tempVal

def my_func2(in1, in2):
    yield in1, in2
    return




def data_gen():
    t = data_gen.t
    lastTemp = 22
    while True:
       t+=1
       strin = ser.readline()
       val = int(strin)
       #print(val)
       # strinDecoded = strin.decode()
       # tempString = strinDecoded[:2]
       # tempVal = int(tempString)
       # val = tempVal
       # print(val)
       #strin = ser.readline()
       yield t, val



def data_gen2():
    t = data_gen.t
    lastTemp = 22
    while 1:
        strin = ser.readline()
        strinDecoded = strin.decode()
        tempString = strinDecoded[:2]
        tempVal = int(tempString)
        if (tempVal < lastTemp - 2):
            tempVal = lastTemp
        else:
            lastTemp = tempVal
        if (tempVal > lastTemp + 2):
            tempVal = lastTemp
        else:
            lastTemp = tempVal
        print(tempVal)
        lastTemp + random
        yield t, tempVal


def run(data):
    # update the data
    t, y = data
    if t > -1:
        xdata.append(t)
        ydata.append(y)
        if t > xsize:  # Scroll to the left.
            ax.set_xlim(t - xsize, t)
        line.set_data(xdata, ydata)

    return line,


def on_close_figure(event):
    sys.exit(0)

data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_ylim(10, 65)
ax.set_xlim(0, xsize)
ax.grid()
xdata, ydata = [], []
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=100, repeat=False)
plt.show()
# =================================================================

