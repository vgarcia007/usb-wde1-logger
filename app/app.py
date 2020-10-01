import serial, sys, signal, time, syslog, json

serialPort='/dev/ttyUSB0'
destination_file = '/home/pi/a-pi-api/app/wde1.json'

while True:
    try:
        ser = serial.Serial(serialPort,baudrate=9600,timeout=None)
    except serial.SerialException as e:
        syslog.syslog(str(e)+". Exiting.")

    serData = ser.readline()
    ser.close()

    dataset = serData.decode().split(";")

    weather_data = {}
    weather_data["timestamp"]=time.time()
    
    for n in range(1,9):
        weather_data["temp"+str(n)]=dataset[2+n].replace(",",".")
        weather_data["hum"+str(n)]=dataset[10+n].replace(",",".")
        
    weather_data["temp9"]=dataset[19].replace(",",".")
    weather_data["hum9"]=dataset[20].replace(",",".")
    weather_data["windspeed"]=dataset[21]
    weather_data["rainfall"]=dataset[22]
    weather_data["rain"]=dataset[23]

    with open(destination_file, 'w') as outfile:
        json.dump(weather_data, outfile)

