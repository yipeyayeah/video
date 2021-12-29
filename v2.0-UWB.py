import time
import serial
import csv
import datetime

header = ['Time', 'Parameter 1', 'Parameter 2', 'Parameter 3', 'Parameter 4', 'Parameter 5', 'Parameter 6']

ser = serial.Serial()
ser.port = 'dev/ttyACM1' # Raspberry Pi top right port
#ser.port = 'COM4'  # Windows Port Setting

ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1
ser.open()

# \r is the escape character for Enter
ser.write(b'\r\r')
# ser.write(b'les\r')

with open('Results-UWB-New.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # print(data)
   

    while True:
        try:

            rawInput = str(ser.readline())
            if not (len(rawInput)<20):
                dateTime = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]

                tmpData = dateTime + ' ' + str(ser.readline())
                tmpData = tmpData.replace("b'", "")
                tmpData = tmpData.replace("'", "")
                tmpData = tmpData.replace("\\r\\n", "")

                data = tmpData.split()
                writer.writerow(data)
                print(tmpData)
                # data.append(tmpArray)

            time.sleep(0.1)
        except Exception as e:
            print(e)
            pass
        except KeyboardInterrupt:
            ser.close()

