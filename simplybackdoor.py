import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.1.4", 4444))

connection.send(b"\n[+] Connection established\n")

recieved_data = connection.recv(1024)
print(recieved_data)

connection.close()