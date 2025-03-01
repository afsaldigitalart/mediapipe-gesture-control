import serial.tools.list_ports 
import serial
import time


class Arduino():
    #Automatically checks which port has the arduino connected and starts serail communication
    def __init__(self):
        self.port = self.checkPort()
        self.arduino = serial.Serial(self.port, 9600)

    def send_to_arduino(self, command):
        try:
            if self.arduino.is_open:
                self.arduino.write(((command+"\n").encode())) #Added new line (\n) so arduino can identify each characters
                time. sleep(0.01)  #to avoid overloading

        except serial.SerialException:
            pass

    def checkPort(self):

        ports = serial.tools.list_ports.comports()
        names = ["arduino", "ch340", "usb serial"]
        for port in ports:
            for name in names:
                if name in port.description.lower():
                    return port.device 
        return None