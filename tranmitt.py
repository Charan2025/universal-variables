from pyPS4Controller.controller import Controller
import serial
import variablesPy
class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.port = "/dev/ttyS0"
        self.baudrate = 115200
        self.timeout = 1 
        self.stopbits = serial.STOPBITS_ONE
        self.ser = serial.Serial(self.port, self.baudrate, parity=serial.PARITY_NONE, stopbits=self.stopbits, bytesize=serial.EIGHTBITS, timeout=self.timeout)
       
        packet = variablesPy.total
        self.ser.write(packet)
        
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

