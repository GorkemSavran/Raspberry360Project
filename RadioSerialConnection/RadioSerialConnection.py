import threading
import serial

class RadioSerialConnection(threading.Thread):

    def __init__(self, derece0, derece1):
        threading.Thread.__init__(self)
        self.daemon = True
        self.__isKilled = threading.Event()
        self.connection = serial.Serial("/dev/ttyUSB0")
        self.derece0 = derece0
        self.derece1 = derece1
        self.start()


    def run(self):
        while not self.__isKilled.isSet():
            line = self.connection.readline()
            derece_num, derece = line.split()
            if derece_num == b'DERECE0':
                self.derece0.set(derece)
            else:
                self.derece1.set(derece)

    def kill(self):
        self.__isKilled.set()
        self.join()