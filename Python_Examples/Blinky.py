import serial
from time import sleep

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
    def pacman(self):
        self.ser.write("$$$T1,1.Z\r")


def main():
    pi = PiLiteBoard()
    pi.pacman()

if __name__ == "__main__":
    main()