import socket
import threading
import time
import os


# ExitCommand class, signal_handler() adapted from


class ExitCommand(Exception):
    pass


def signal_handler(signal, frame):
    raise ExitCommand()


FORMAT = 'utf-8'
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER= '127.0.0.1'
PORT= 64444


def send(client, msg):
    # global receive_thread
    message = msg.encode(FORMAT)
    client.send(message)
    # if message == '!q':
    #     os.kill(receive_thread.native_id, signal.SIGTERM)
    #     exit(0)

    
def receive(client):
    while True:
        print(client.recv(2048).decode(FORMAT))
        
def usernaming(client):
    print("Enter your name: ")
    name = input()
    send(client, name)
    flag = client.recv(2048).decode(FORMAT)
    
    return(flag)

def main():
    #print("Enter your name: ")
    #name = input()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    while (True):
        #calling the usernaming function to take username from user and perform naming conventions
        flag = usernaming(client)
        if(flag != 'You are in the lobby.'):
            print(flag)
            
        else:   
            # Specifies a second thread.  Loops infinitely inside receive()
            receive_thread = threading.Thread(target=receive, args=(client,))
            receive_thread.start()
            break

    while True:
        msg = input()
        send(client, msg)


if __name__ == "__main__":
    main()
