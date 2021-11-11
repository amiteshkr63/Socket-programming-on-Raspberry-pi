import socket
import sys
import RPi.GPIO as GPIO

#Creating a server socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding server socket to IP address and port
try:
    mysock.bind(("",1234))#empty IP field(client or host) so any IP with port 1234 can make connection to server socket
except socket.error():
    print("Failed to Bind")
    sys.exit()

#Listen() listening for some client.connect() and listen argument:'BACKLOG' means how many requests allowed to wait for service
mysock.listen(5)

'''
Accepting a connection request means, accepting the call to connect from the client
accept() accept a connection request and accept() returns 2 arguments:(1)A connection(for sending/receiving)
                                                                      (2)an address(IP,port)
'''

while True:
    conn, addr=mysock.accept()
    data=conn.recv(1000)
    if (not data):
        continue
    else:
        print("Got a Reuest!")
            
    
conn.close()
mysock.close()




