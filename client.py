#!/usr/bin/env python

import select, socket, sys
import socket
import time
from tkinter import *

## Get the Local IP through the google server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("8.8.8.8", 443))
TCP_IP = s.getsockname()[0]
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_PORT = 5001
BUFFER_SIZE = 1024
s.connect((TCP_IP, TCP_PORT))

print ("The server is connected. Please type the command line.")

## Input command lines and received by server
inputs = [s, sys.stdin]
newData = 0

while inputs:
    readable, writable, exceptional = select.select(inputs, inputs, inputs)
    for socket in readable:
        if socket is s:
            data = s.recv(1024)
            window = Tk()
            window.title("Receive a message")
            window.geometry('350x200')
            lbl = Label(window, text = (data.decode()))
            lbl.grid(column = 0, row = 0)
            window.mainloop()
            print(data.decode())
        elif socket is sys.stdin:
            print ("The data in command line is received.")
            msgToSend = input()
            s.sendall(msgToSend.encode())

f.close()
s.close()
