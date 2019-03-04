import serial

ser = serial.Serial(
timeout=0.050,
port='COM6',
baudrate=115200,
parity=serial.PARITY_ODD,
stopbits=serial.STOPBITS_TWO,
bytesize=serial.SEVENBITS)

print(ser.isOpen())

######### Read APN
#ser.write("AT\r\n".encode())
ser.write('AT+CGDCONT?\r\n'.encode())

while True:
        response =(ser.readline())
        if response == b'':
            break
        print (response)

    
######## Write APN
print('**********************')
ser.write('AT+CGDCONT=1,"IP","internet.vodafone.net","0.0.0.0",0,0,0,0\r\n'.encode())



######## Read APN Again
ser.write('AT+CGDCONT\r\n'.encode())
print('----------------------')
while True:
        response1 =(ser.readline())
        if response1 == b'':
            break
        print (response1)
