import socket

client = socket.socket()
print("Clients socket has been created")

client.connect(('127.0.01', 8888))
print("Client's socket has been connected to the server")

message = input("Enther the message for the server\n")
client.send(message.encode())
print("The message '{0}' has been sent to the server".format(message))

data = client.recv(1024)
print("The message has been recieved")
print(data.decode())

client.close()
print("Client's socket has been closed")