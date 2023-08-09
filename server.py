from cgitb import reset
import socket  # allows bidirectional connection
from _thread import *  # allows accepting new clients while processing already-connected clients
import pickle
from xml.etree.ElementTree import TreeBuilder
from game import Game

HOST = "localhost"
PORT = 5555

connected = set()  # store ip addr's of connected clients
games = {}  # disctionary to store id and game object pairs
client_cnt = 0  # track how many clients are connectedto to the server

# run in the background
def threaded_client(conn, p, gameID):
    global client_cnt
    conn.send(str.encode(str(p)))  # which player this client is

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameID in games:
                game = games[gameID]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_game()
                    elif data != "get":
                        if (p == 1 and game.p1Went) or (p == 2 and game.p2Went):
                            game.lock = True
                        else:
                            game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connection")
    print("Closing Game", gameID)
    try:
        del game[gameID]
    except:
        pass
    client_cnt -= 1
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()  # listen for incoming client
        print("Connected to: ", addr)

        client_cnt += 1
        p = 1
        gameID = (client_cnt - 1) // 2  # integer division (//) = floor division
        if client_cnt % 2 == 1:
            games[gameID] = Game(gameID)
            print("Creating a new game...")
        else:
            games[
                gameID
            ].ready = True  # both players are connecte -> game ready to start
            p = 2

        start_new_thread(threaded_client, (conn, p, gameID))
