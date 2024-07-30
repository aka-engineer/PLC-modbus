import minimalmodbus
from serial import Serial

client = minimalmodbus.Instrument("COM10", 1, mode=minimalmodbus.MODE_RTU, close_port_after_each_call=True)

# data = client.read_registers(4970, 20, 3)

# print (data)