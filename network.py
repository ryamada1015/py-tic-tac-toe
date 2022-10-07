import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.47"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()  # receive and return player
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))  # send string data to server
            return pickle.loads(
                self.client.recv(2048)
            )  # receive object data back from server
        except socket.error as e:
            print(e)
