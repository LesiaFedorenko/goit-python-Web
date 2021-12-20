import socket
import threading

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('127.0.0.1', 1231))
soc.listen(2)

users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_user(user, address):
    while True:
        data = user.recv(2048)
        print(f'User {address[1]} sent {data}')

        send_all(data)


def start_server():
    print('Chatroom')
    while True:
        user_socket, address = soc.accept()
        print(f'User {address[1]} connected')

        users.append(user_socket)
        listen_concurrently = threading.Thread(
            target=listen_user,
            args=(user_socket, address,))
        listen_concurrently.start()


if __name__ == '__main__':
    start_server()
