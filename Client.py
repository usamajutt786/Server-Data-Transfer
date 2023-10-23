import socket
s = socket.socket()
port = 8080
host = input("Please enter the host address of the sender: ")
s.connect((host,port))
print("Connected...")
filename = input("Please enter a filename for the incoming file: ")
file = open(filename, 'wb') # Opens a file for writing only in binary format
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")