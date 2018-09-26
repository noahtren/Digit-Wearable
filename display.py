import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

code_epochs = [["HL", "L", "L"],
["HL", "HL", "L"],
["H", "L","L"],
["H", "LH", "L"],
["HL", "LH", "L"],
["H", "HL", "L"],
["H", "H", "L"],
["HL", "H", "L"],
["LH", "HL", "L"],
["H", "H", "L"],
["HL", "L", "HL"],
["HL", "HL", "HL"],
["H", "L","HL"],
["H", "LH", "HL"],
["HL", "LH", "HL"],
["H", "HL", "HL"],
["H", "H", "HL"],
["HL", "H", "HL"],
["LH", "HL", "HL"],
["LH", "H", "HL"],
["LH", "L", "H"],
["HL", "HL", "H"],
["LH", "H", "LH"],
["H", "L", "H"],
["H", "LH", "H"],
["HL", "LH", "H"],
["L", "L", "L"]]
code_map = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def pad(array, target_len):
    padded = np.append(array, [0]*(target_len - len(array)))
    return padded

def fill(start, finish, count):
    if (start == finish):
        return np.full(count, start)
    else:
        return np.arange(start, finish, (finish-start)/(count-0.5))

def encode_string(string):
    code_index = list(string)
    code = list(string)
    for i in range(0, len(string)):
        code_index[i] = code_map.index(string[i])
        code[i] = code_epochs[code_index[i]]
    return code

# 100 microsecond resolution for each value
# (time in miliseconds * 10) / 4 = epoch length in 100 microsecond increments
def gen_data(str, dur):
    unit_array = encode_string(str)
    data = []
    for unit in unit_array:
        for epoch in unit:
            if (epoch == "L"):
                data = np.append(data, fill(40, 40, math.floor((dur*10)/4)))
            elif (epoch == "H"):
                data = np.append(data, fill(150,150,math.floor((dur*10)/4)))
            elif (epoch == "LH"):
                data = np.append(data, fill(40,150,math.floor((dur*10)/4)))
            elif (epoch == "HL"):
                data = np.append(data, fill(150,40,math.floor((dur*10)/4)))
        data = np.append(data, fill(0, 0, math.floor((dur*10)/4)))
    t = np.arange(1, len(data)+1, 1)
    data = (data, t)
    return data

def disp_data(s, t):
    fig, ax = plt.subplots() 
    ax.plot(t, s)
    ax.set(xlabel='Time (100 microsecond steps)', ylabel='Frequency (Hz)',
       title='Vibration Speaker Frequency')
    plt.ylim(-5,155)
    plt.xlim(0, len(t))
    ax.grid()
    plt.show()

# unit duration is the amount of time, in milliseconds, that
# a unit of meaning will take
# wpm = 12000/unit_duration
# unit duration of 100: 120 wpm
# unit duration of 50: 240 wpm
# unit duration of 200: 60 wpm

unit_duration = 1000
(s, t) = gen_data("hello world", unit_duration)
disp_data(s, t)