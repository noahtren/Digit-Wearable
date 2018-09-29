import time
import display
from appJar import gui

# Stream represents the string that is being read through
# the object saves the string and the reader's position in
# the string
class Stream:
    def __init__(self, str, index):
        self.string = str.replace(" ", "_")
        self.index = index
        self.data = display.gen_data(self.string)
    def refresh(self, length):
        segment = self.string[self.index:self.index+length]
        return segment
    def iterate(self, direction):
        self.index += direction

# The reader class calls functions from the Stream
# and allows for the user to control the experience
class Reader:
    def __init__(self, rate, length, direction):
        self.rate = rate
        self.length = length
        # reading direction is 1 for right, 0 for pause, and -1 for left
        self.direction = direction
    def read(self, stream):
        string = stream.refresh(self.length)
        # INSERT CODE HERE FOR WRITING TO DEVICE
        print(string)
        time.sleep(self.rate)
        self.educate(stream)
        stream.iterate(self.direction)
        # return this if the end of the stream has been reached
        # 1 is a sign to continue, while a 0 says you should stop
        if (stream.index >= (len(stream.string)-self.length)+1):
            return 0
        else:
            return 1
    def educate(self, stream):
        app = gui("Digit Display")
        for i in range (1, self.length):
            app.addLabel(str(i), stream.refresh(self.length)[i-1])
        app.setFg("black")
        app.setBg("white")
        app.setFont(size=32, family="Arial")
        app.setLocation("CENTER") 
        app.go()


s = Stream("testing", 0)
r = Reader(0.1, 6, 1)

d = display.gen_data(s.string)
display.disp_data(d)

while 1:
    if r.read(s) == 0:
        break
r.read(s)

