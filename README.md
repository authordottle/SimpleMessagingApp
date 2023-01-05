
# Message App
## Jiaqian Huang.2366

# What makes it
## Files: one client.py, one server.py, and db.txt for database
## UI: Tkinter 
## ** Notice: In this project, the notification will pop up in the window. The user needs to turn off the window to see the next message. 
## ** Notice: If multiple clients run on the local IP, users can check their messages in the terminal clearly after closing the window in case they don't know whom those windows belong to. If clients run on different laptops, windows can be enough.

# What to require
## python3
## Need to run on the MAC/Linux
## Operate on the same laptop

# How to start

## ln the terminal:
## Open the server.py
## $ python3 server.py

## ln another terminal:
## Open the client.py
## $ python3 client.py
## ** Notice: More connections can be made by adding running client.py in other terminals.

## To login:
## $ login username password
## **Notice: A notification will pop up to warn the user if the user inputs a non-existed userID or wrong password.

## To register:
## $ register username password
## **Notice: A notification will pop up to warn the user if the userID already existed.

## After login send the message:
## $ msg username message_data
## **Notice: A notification will pop up to warn the user if the user is not logged in or is not online.

## To log out:
## $ logout username
## ** Notice: Still need to use the ^C to stop the client.py in this terminal, logout command line here only helps make user offline.

## ** Notice: Assume no same user logged into the different terminals, command line inputs are following the format above



