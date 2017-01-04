# Reverse-Shell
A Simple server, client reverse shell based on a tutorial by theNewBoston, but customized and improved (to some extend).

These two scripts create a connection between two devices, a server and a client, 
which can be used to send commands and responses back and fourth.

First, the server script needs to be run to create the socket, bind it to a port and listen for clients.

Second, the client script is run on another device (althoguh all current testing has been done locally),
which connects to the IP and port of the server (currently hardcoded to simplify testing).

Third, the established connection is displayed on the serverside, and starts reading in any commands.
The tricky part is reading in the console input and encodin it properly, and then decoding it on the client side.
Currently there is an issue with the 'cd' command, somthing related to a '\n' character that must be read in somewhere,
check out 'Issues' for more!

The Goal for this is to create a dummy-proof server-client relationship that get's as close to a locally run command propt as possible. The tricky thing here will be determining what the limitations might be, they should all be related to decoding the server-sent data and running it on the client, or sending back the output that might be hard to obtain from the client to the server. For example: running 'nano test.txt' will be hard to do, because the nano interface won't be send back to the server. 
Running a command like that would leave the server 'blind'.

I'm mostly putting this up to learn more about github :)

