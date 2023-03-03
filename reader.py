import serial
import time
import requests

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM11', 9600, timeout=1)
time.sleep(2)
start = time.time()
num = 0
url = 'http://35.199.80.231:8080/mesurements/update/1/'



while num != 10:
    
    line = ser.readline()  

    if line:
        string = line.decode().strip()  
        n_num = string.split(",") 
        print(n_num)
        if len(n_num) == 6:
            myobj = {"temperatura":n_num[0], "humedad":n_num[1], "presion":n_num[2], "altura":n_num[3],"ppm":n_num[4]}

            x = requests.put(url, json = myobj)
            print(x.text)
                   
ser.close()