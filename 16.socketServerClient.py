# 플랜.
# 소켓 서버를 씌우고 ..
# 소켓 서버는 접속하면 Thread 로 client 와 통신.
# 소켓 서버를 띄우고 난 후 클라이언트를 띄운다. (원래는 분리인데 여긴 테스트니까 같이 돌린드아...)
# 클라이언트 2개 생성.
# 하나는 접속하고 대기타는 넘.. (게임로직...)
# 또하나는 접속하고 바로 종료해 버림 ... (2개 이상의 쓰레드를 발생시켜 볼라고 시도..)
# 서버는 더이상 접속자가 없으면 2초뒤 종료됨 ...

import asyncio
import socket
import time
import threading

def client_thread(conn, addr):
    conn.sendall(b'welcome')

    while True:
        data = conn.recv(1024)
        print( type(data))
        if not data:
            break
        conn.sendall(data)
    conn.close()

def start_server():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)     # 최대 연결 수 지정.

    print('--server Start--')

    while True:
        conn, addr = server_socket.accept()
        print('Connected by', addr)
        threading.Thread(target=client_thread, args=(conn, addr)).start()

def start_client():
    host = '127.0.0.1'
    port = 5000

    print('--client start--')

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input('Enter message: ')
        # 입력을 비동기식으로 처리해야 할 것 같다 .... input 단계에서 멈춰있는 상태임...

        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print('Received', repr(data.decode()))


if __name__ == '__main__':
    # asyncio.run( start_server() ) # 일케하면 안되지 ... 밑으로 넘어가질 않으니 ....
    threading.Thread(target=start_server).start()

    time.sleep(2)
    print('now client run')
    start_client()


