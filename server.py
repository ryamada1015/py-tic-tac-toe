import socket  # allows bidirectional connection
from _thread import *  # allows accepting new clients while processing already-connected clients
import sys

server = "10.0.0.47"
port = 5555

# run in the background
def threaded_client(conn):
    conn.send(
        str.encode("Connected")
    )  # send some message back to the client to notify the connection has been successful
    reply = ""
    while True:
        try:
            # 2048 = amount of data to receive
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            # if not received data
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server, port))
    s.listen(2)
    print("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)

        start_new_thread(threaded_client, (conn,))

