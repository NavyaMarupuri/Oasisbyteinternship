import socket
import threading

def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received from {address}: {message}")
        client_socket.send("Message received".encode('utf-8'))

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)

    print("Server listening on port 12345...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))

    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

    client.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    client_thread = threading.Thread(target=start_client)
    client_thread.start()
