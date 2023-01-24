
import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
import datetime as dt
import serial
# board1 = serial.Serial(port='/dev/cu.usbmodem1301', baudrate=400000)
board2 = serial.Serial(port='/dev/cu.usbserial-120', baudrate=200000)
plt.ion()
Mode = 'drow'#'Detection'
fig, ax_l = plt.subplots(2, 1)

def read_b(plata):
    data = plata.read(2)
    # print(int.from_bytes(data[::-1], 'big'))
    return int.from_bytes(data[::-1], 'big')

while True:
    start = True
    Flag = True
    delta = dt.timedelta(seconds=1)
    t1 = dt.datetime.now()
    s1, s2 = [], []
    # read_b(board1)
    read_b(board2)
    while Flag == True:
        # s1.append(read_b(board1))
        s2.append(read_b(board2))
        if dt.datetime.now() - t1 > delta:
            Flag = False

    # s1 = np.array(s1)
    s2 = np.array(s2)
    print('freq',len(s1),len(s2))
    # if (len(s1)>1) and (len(s2)>1):
    if (len(s2)>1):
        # ax_l[0].plot(s1)
        ax_l[1].plot(s2)
        plt.show()
        plt.pause(0.001)
        for ax in ax_l:
            ax.clear()
