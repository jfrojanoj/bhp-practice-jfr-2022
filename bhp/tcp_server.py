"""Taken from the book Black Hat Python."""

import socket
import threading

IP = "0.0.0.0"
PORT = 9998


def main():
    """Run main function IPv4 TCP."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))  # ip and port to listen to
    server.listen(5)  # maximum backlog conecctions
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    """Handle client sockets."""
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")


if __name__ == "__main__":
    main()
