import serial
import time
import sensor_lib
import codecs

sensor = sensor_lib.DFRobot_mmWave_Radar('/dev/serial0')


try:
    """sensor._s.write("sensorStop".encode())
    time.sleep(1)"""
    '''sensor._s.write("setUartOutput 2 1".encode())
    time.sleep(1)
    sensor._s.write("setUartOutput 1 0".encode())
    time.sleep(1)'''
    '''sensor._s.write("setLatency 0 0".encode())
    time.sleep(1)
    sensor._s.write("factoryReset 0x45670123 0xCDEF89AB 0x956128C6 0xDF54AC89".encode())#("factoryReset "+" "+codecs.decode("45670123", 'hex').decode('utf-8')+" "+codecs.decode("CDEF89AB", 'hex').decode('utf-8')+" "+codecs.decode("956128C6", 'hex').decode('utf-8')+" "+codecs.decode("DF54AC89", 'hex').decode('utf-8')).encode(encoding="ascii"))
    time.sleep(1)
    sensor._s.write("setRange 0 0.5".encode())
    time.sleep(1)'''
    '''sensor._s.write("getLatency ".encode())
    time.sleep(1)
    sensor._s.write("getRange".encode())
    time.sleep(1)
    sensor._s.write("getSensitivity".encode())
    time.sleep(1)
    sensor._s.write("setLatency 0 0".encode())
    time.sleep(1)'''
    '''sensor._s.write("setRange 0 0.7".encode())
    time.sleep(1)
    sensor._s.write("setSensitivity 6".encode())
    time.sleep(1)
    
    sensor._s.write("resetSystem".encode())
    time.sleep(1)
    sensor._s.write("getRange".encode())
    time.sleep(1)
    sensor._s.write("getLatency ".encode())
    time.sleep(1)
    sensor._s.write("getSensitivity".encode())
    time.sleep(1)
    
    sensor._s.write("setLedMode 1 1".encode())
    time.sleep(1)
    sensor._s.write("setSensitivity 5".encode())
    time.sleep(1)
    sensor._s.write("saveCfg 0x45670123 0xCDEF89AB 0x956128C6 0xDF54AC89".encode())
    time.sleep(1)
    sensor._s.write("sensorStart".encode())
    time.sleep(1)'''
    
    #Get system saved configs
    sensor.getLatency()
    sensor.getRange()
    sensor.getSensitivity()
    sensor.getLedMode()
    sensor.getUartOutput(1)
    
    sensor.sensorStop()
    sensor.setRange(0, 1)
    sensor.setSensitivity(7)
    sensor.setLatency(0,0)
    sensor.setUartOutput(1,0,0,1)
    sensor.setUartOutput(2,1,0,1)
    sensor.setLedMode(1)
    sensor.saveConfig()
    sensor.sensorStart()
    
    #sensor.factoryReset()
    #sensor.DetRangeCfg(0,0.3)
    #sensor.OutputLatency(0,0)
    while True:
        #print(sensor.readData())
        #time.sleep(1)
        #val = sensor.readPresenceDetection()
        #print(f"Received: {val}")
        data = sensor.readData()
        if data != None:
            print(data)
        '''if sensor._s.in_waiting > 0:
            data = sensor._s.readline().decode('utf-8').strip()
            print(f"Received: {data}")'''
          
        '''if sensor.readPresenceDetection():
            print("Presence detected")
        else:
            print("No presence detected")
          '''
       # time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    sensor._s.close()
