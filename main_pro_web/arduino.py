import simplejson as sj
import serial as s
import time as t

ser = s.Serial('/dev/ttyACM0', 9600)

while 1:
    print 'running'
    t.sleep(.5)
    f = open('light_data.txt','r')
    arr = sj.loads(f.read())
    f.close()
    if arr['light_1']==1:
        ser.write('1')
    else:
        ser.write('4')
    if arr['light_2']==1:
        ser.write('2')
    else:
        ser.write('5')
    if arr['light_3']==1:
        ser.write('3')
    else:
        ser.write('6')
