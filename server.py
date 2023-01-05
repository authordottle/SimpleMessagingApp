#!/usr/bin/env python

import select, socket, sys
import threading
import urllib.request

user_name = []
socket_list = []
conn_list = []
user_connection = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(("", 5001))
server.listen(5)

inputs = [server, sys.stdin]
newData = 0
conns = 0
isLogin = False
isPrinted = False

## Import the db with updates
def importDB():
    db = dict()
    f = open("db.txt","r+")
    for line in f:
        if line != "\n":
            userInfo, password = str(line).split(",")
            password = password.split("\n")[0]
            db[userInfo] = password
    return db

## Print out the active users
def printActiveUsers():
    for i,user in enumerate(user_connection):
        for connection in conn_list:
            connection.send((user + " is online. ").encode())

## Print out the disconnected users
def printDisconnections(user):
    for connection in conn_list:
        connection.send((user + " is offline. ").encode())

## Main Function
while inputs:
    db = importDB()
    readable, writable, exceptional = select.select(inputs, inputs, inputs)
    for s in readable:
        if s is server:
            print ("Here receives a connect request from a client. ")
            print
            conn, addr = s.accept()
            if conns == 0:
                conns = 1
                conn1 = conn
            else:
                conn2 = conn
            print ("Connection is {}".format (conn))
            conn.setblocking(0)
            inputs.append(conn)
            conn_list.append(conn)
            localConn = conn
        elif s is sys.stdin:
            newData = 1;
            command_string = input()
            print ("Received:::: " + command_string)
        else:
            data = s.recv(1024).decode()
            if data:
                print ("Reading the data sent from users: " + data)
                words = data.split()
                print ("Received the data: " + data + "")
                for i,word in enumerate(words):
                    if word == "login":
                        userID = words[i+1]
                        password = words[i+2]
                        if userID in db:
                            if (password == db[userID]):
                                isLogin = True
                                user_connection[userID] = s
                                greetingMessage = "Let's start to chat.\n"
                                localConn.send (greetingMessage.encode())
                                printActiveUsers()
                            else:
                                errorMessage = "The password is not correct."
                                localConn.send (errorMessage.encode())
                        else:
                                errorMessage = "The userID does not exist."
                                localConn.send (errorMessage.encode())
                    elif word == "msg":
                        if (isLogin):
                            receivedUserID = words[i+1]
                            msg = " ".join(str(x) for x in words[i+2:])
                            if receivedUserID in user_connection:
                                send_sock = user_connection[receivedUserID]
                                send_sock.send (msg.encode())
                            else:
                                errorMessage = "The user is not online."
                                localConn.send (errorMessage.encode())
                        else:
                            errorMessage = "Please log in first."
                            localConn.send (errorMessage.encode())
                    elif word == "register":
                        userID = words[i+1]
                        password = words[i+2]
                        if not userID in db:
                            with open("db.txt", "a") as f:
                                f.write(userID +","+ password +"\n")
                                greetingMessage = "Ok. "+ userID +" is registered now."
                                localConn.send (greetingMessage.encode())
                        else:
                            errorMessage = "The userID already exists."
                            localConn.send (errorMessage.encode())
                    elif word == "logout":
                        if isLogin:
                            userID = words[i+1]
                            conn_list.remove(user_connection[userID])
                            del user_connection[userID]
                            isLogin = False
                            printDisconnections(userID)
                        else:
                            errorMessage = "The user is not login."
                            localConn.send (errorMessage.encode())
                        
                if newData == 1:
                    data = command_string
                    newData = 0
                print ("User-connection: \n", user_connection)

    for s in exceptional:
        inputs.remove(s)
        print(inputs)
        if s in outputs:
            outputs.remove(s)
        s.close()

f.close()
