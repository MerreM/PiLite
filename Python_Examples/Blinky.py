import serial
from time import sleep

class PiLiteBoard(object):
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
        self.ser.write("$$$SPEED50\r")
    def write(self, text):
        text = text.encode('utf-8')
        while text:
            self.ser.write(text[:14])
            text = text[14:]
            sleep(3)
    def pacman(self):
        self.ser.write("$$$F000000000000000000000111000011111110011111110111111111111101111111101111011000110011000110000000000000000000000000000000000000")


def main():
    pi = PiLiteBoard()
    pi.pacman()

if __name__ == "__main__":
    main()