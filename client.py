import socket              

s = socket.socket()
host = '192.168.0.18'
port = 80

s.connect(socket.getaddrinfo(host, port)[0][-1])

if __name__ == '__main__':
    while True:
        msg = input('--->>> ') 
        s.sendall(msg)