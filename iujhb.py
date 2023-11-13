import socket
import requests


class Server:
    def __init__(self):
        self.server_socket = None

    def disconnect(self):
        print("disconnecting")
        self.main()

    def main(self):
        client_socket, client_address = self.server_socket.accept()
        while True:
            data = client_socket.recv(1024)
            if len(data) == 0:
                self.disconnect()
            print(f"data:\n{data.decode()}")

    def start(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(("127.0.0.1", 80))
        self.server_socket.listen()
        self.main()


    @staticmethod
    def check_http(req):
        list_of_req = str(req).split()
        cmd_itself = list_of_req[0]
        url = requests.get(req[1])
        protocol_ver = req[2]
        if cmd_itself == "GET " and url and " " and protocol_ver == r"HTTP/1.1\r\n" or protocol_ver == r"HTTP/1.1\r\n\r\n":
            return True
        return False


if __name__ == "__main__":
    app = Server()
    app.start()