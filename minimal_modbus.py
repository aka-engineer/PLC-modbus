import minimalmodbus
from def_servo import *
from serial import Serial
import time

ser = Serial('COM11', baudrate=9600, bytesize=7, parity='E', stopbits=1)
client = minimalmodbus.Instrument(ser, 1, mode=minimalmodbus.MODE_ASCII, close_port_after_each_call=False)

client.write_bit(MODE_JOG_POSITION, 0)
client.write_bit(RUN_POSITION, 1)
client.write_bit(MANUAL_CHECK, 1)
client.write_long(SPEED_SERVO1, 3000, byteorder=minimalmodbus.BYTEORDER_LITTLE_SWAP)
client.write_bit(MANUAL_CHECK, 0)

while True:
    client.write_long(SET_POSITION_SERVO1, 500000, byteorder=minimalmodbus.BYTEORDER_LITTLE_SWAP)
    data = client.read_long(SET_POSITION_SERVO1, byteorder=minimalmodbus.BYTEORDER_LITTLE_SWAP)
    print(data)
    time.sleep(5)
    client.write_long(SET_POSITION_SERVO1, 0, byteorder=minimalmodbus.BYTEORDER_LITTLE_SWAP)
    data = client.read_long(SET_POSITION_SERVO1, byteorder=minimalmodbus.BYTEORDER_LITTLE_SWAP)
    print(data)
    time.sleep(5)

data = client.read_registers(4590, 50, 3)
print (data)

data = client.read_bits(2049, 50, 1)

print (data)
client.serial.close()
ser.close()