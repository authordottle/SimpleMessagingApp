
# Messaging App
#### J H

# What makes it
#### Files: one client.py, one server.py, and db.txt for database
#### UI: Tkinter 

<br />** Notice: In this project, the notification will pop up in the window. The user needs to turn off the window to see the next message. 
<br />** Notice: If multiple clients run on the local IP, users can check their messages in the terminal clearly after closing the window in case they don't know whom those windows belong to. If clients run on different laptops, windows can be enough.

# Prerequisite
1. Version: python3 <=
2. Same MAC/Linux Only

# How to start
1. ln the terminal, cd into server folder and open the server.py
```
{versionOfPython} server.py
```

2. ln another terminal, cd into server folder and open the client.py
```
{versionOfPython} client.py
```
** Notice: More connections can be made by adding running client.py in other terminals.

3. To login:
```
login {username} {password}
```
**Notice: A notification will pop up to warn the user if the user inputs a non-existed userID or wrong password.

4. To register:
```
register {username} {password}
```
**Notice: A notification will pop up to warn the user if the userID already existed.

5. After login send the message:
```
msg {username} {message_data}
```
**Notice: A notification will pop up to warn the user if the user is not logged in or is not online.

6. To log out:
```
logout {username}
```
** Notice: Still need to use the ^C to stop the client.py in this terminal, logout command line here only helps make user offline.

<br />** Notice: Assume no same user logged into the different terminals, command line inputs are following the format above

# Feedback
#### Need to allow client on machine 1, client on machine 2, server on machine 3, which means the client will ask the IP (and port) of server.

