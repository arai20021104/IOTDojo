import socket
port = 80
ListenSoket = None
ip = wifi.ifconfig()[0]
listenSocket = socket.socket()
listenSocket.bind((ip, port))
listenSocket.listen(5)
listenSocket.setsockept(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)

while True:
    print("accepting.....") 
    conn, addr = listenSocket.accept()
    print(addr, "connected")
    while True:
        data = conn.recv(1024)
        if(len(data) == 0):
            print("close socket")
            conn.close()
            break
        print(data)