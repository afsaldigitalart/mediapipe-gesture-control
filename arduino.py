import serial.tools.list_ports 
import serial
import time


class Arduino():
    def __init__(self):
        #Connects to the Arduino
        self.port = self.checkPort()
        self.arduino = serial.Serial("COM8", 9600)

    def send_to_arduino(self, command):
        try:
            if self.arduino.is_open:
                self.arduino.write(((command+"\n").encode()))
                time. sleep(0.01)  

        except serial.SerialException:
            pass

    def checkPort(self):

        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description:
                return port.device 