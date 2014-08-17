import socket
import time
import sys
import threading
#import serial

#ser = serial.Serial('/dev/ttyUSB0',115200)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IPADRESS = "192.168.1.142"
PORT = 6000

def socket_connect(sockConnect):
	i = 0
	while i <10:
		try:
			print "Connecting"
			sockConnect.connect((IPADRESS,PORT))
			print "Sacesfully connected to IP {ipAdress} and port {port}".format(ipAdress = IPADRESS,port = PORT)
			i = 10
		except socket.error as e:
			print "connection error"
			time.sleep(2)
			i = i+1
	if i == 9: 
		return 0
	if i == 10:
		return 1

					
def socket_send():
	while True:
		time.sleep(0.04);
		try:
			sock.send("1234567890")
		except socket.error as e:
			print "Connection broken on sending"
			break

def socket_receive():
    while True:
        try:
        	data = sock.recv(1024)
        	if not data:
        		raise RuntimeError("socket connection broken")
        	else:
        		print data[0]
        		print data[1:]
        except socket.error as e:
        	print "Connection broken in receieving"
        	break

if __name__ == '__main__':
	if socket_connect(sock) == 0 :
		quit()
	threadSend = threading.Thread(target = socket_send)
	threadSend.start()
	print "threadSend STARTED"
	threadReceive = threading.Thread(target = socket_receive)
	threadReceive.start()
	print "threadReceive STARTED"
    

