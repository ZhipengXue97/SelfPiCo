# Extracted from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def stream_(host):
    import socket
    import ssl
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        context = ssl.create_default_context(Purpose.CLIENT_AUTH)
        with context.wrap_socket(sock, server_hostname=host) as wrapped_socket:
            wrapped_socket.connect((socket.gethostbyname(host), 443))
            wrapped_socket.send(
                "GET / HTTP/1.1\r\nHost:thiscatdoesnotexist.com\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n".encode())

            resp = b""
            while resp[-4:-1] != b"\r\n\r":
                resp += wrapped_socket.recv(1)
            else:
                resp = resp.decode()
                content_length = int("".join([tag.split(" ")[1] for tag in resp.split("\r\n") if "content-length" in tag.lower()]))
                image = b""
                while content_length > 0:
                    data = wrapped_socket.recv(2048)
                    if not data:
                        print("EOF")
                        break
                    image += data
                    content_length -= len(data)
                with open("image.jpeg", "wb") as file:
                    file.write(image)


