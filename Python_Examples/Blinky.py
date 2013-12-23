import serial
from time import sleep

stare  = [
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','#',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' '],
[' ','#','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' '],
['#',' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ','#',' '],
['#',' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ','#',' '],
['#',' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ','#',' '],
[' ','#','#',' ','#','#','#','#',' ','#','#','#',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
]
blink  = [
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['#','#','#','#',' ',' ',' ',' ',' ','#','#','#','#',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ','#','#','#','#',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
]


def faces_to_binary(face):
    output = "$$$F"
    for x in range(14):
        for y in range(9):
            output+='1' if (face[y][x]=='#') else '0'
    return output+"\r"


class PiLiteBoard(object):
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
        self.ser.write("$$$SPEED50\r")
        self.ser.write("$$$ALL,OFF\r")
    def write(self, text):
        text = text.encode('utf-8')
        while text:
            self.ser.write(text[:14])
            text = text[14:]
            sleep(3)
    def stare(self):
        self.ser.write("$$$ALL,OFF\r")
        self.ser.write(faces_to_binary(stare))
    def blinky(self):
        self.stare()
        sleep(3)
        self.blink()
    def blink(self):
        self.ser.write("$$$ALL,OFF\r")
        self.ser.write(faces_to_binary(blink))
        sleep(0.5)
        self.ser.write("$$$ALL,OFF\r")
        self.ser.write(faces_to_binary(stare))

def main():
    pi = PiLiteBoard()
    pi.blinky()

if __name__ == "__main__":
    main()