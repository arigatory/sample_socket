import socket


server = socket.socket()
print("Socket has been created")

server.bind(('127.0.01', 8888))
print('Socet has been bound to the addres')

server.listen()
print('Waiting for income connections')

client , address = server.accept()
print("Client with the address {0} has been connected to the servet".format(address))


data = client.recv(1024)
print("Server got data from the client:")
print(data.decode())

message = "Got your message"
client.send(message.encode())
print("We've sent the message to the client")

client.close()
print("Client's socket has been closed")

server.close()
print("Server's socket has been closed")