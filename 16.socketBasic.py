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
import sys                      # subdirectory 의 module 을 땡기기 위해선 sys도 필요함.
import select   # socket 에서 select 감지를 위해서 ... ( non blocking 처리용 )

# 정상적인 파일 이름이 아닌 dot(.)이 들어간 파일 라이브러리는 import 과정이 복잡해진다.
import importlib.util
spec = importlib.util.spec_from_file_location(
    name="socClient",  # note that ".test" is not a valid module name
    location="./module/16.socketClient.py",
)
socClient = importlib.util.module_from_spec(spec)
spec.loader.exec_module(socClient)
# 위 플로우를 통하여 socClient 에 module 을 로드함.

connection = 0  # 총 연결 갯수를 광역변수로 ..

def client_thread(conn, addr):
    #output = []
    #output.append(b'welcome')
    global connection

    print( '\n--- server thread started', conn, connection, "---\n")
    sys.stdout.flush()
    conn.sendall(b'welcome')

    while True:
        data = conn.recv(1024)
        #print('Received data Type / data From Client : ', type(data), data, str(data, 'utf-8'))
        data_encode = str(data, 'utf-8')
        if not data:
            break
        elif data_encode == '' :
            conn.sendall('data is null'.encode('utf-8'))
        elif data_encode == 'bye':
            conn.sendall( 'Connection Finished'.encode('utf-8') )
            print('client disconnected')
            break
        elif data_encode == 'hello':
            conn.sendall( 'Hi'.encode('utf-8'))

        conn.sendall(data)

        """
        #readBuf, writeBuf, errBuf = select.select([conn], [], [])
        #readBuf, writeBuf, errBuf = select.select([conn], [], [], 1)
        readBuf, writeBuf, errBuf = select.select([conn], output, [])

        for readPacket in readBuf:
            print('input detected', readBuf )
            readP = readPacket.recv(1024)
            print('packet is ..', readP)
            conn.sendall(readP)

        for writePacket in writeBuf:
            conn.sendall(writePacket)
        """

        """
        for readPacket in readBuf:
            #print('Received data Type / data From Client : ', type(readPacket) )
            #print('Data is ', readPacket)
            #data = readPacket.recv(1024)

            data = conn.recv(1024)

            if not data:
                print('NOt')
                break

            print('decode data is', data.decode(), type(data.decode()))

            #if readPacket == b'echo\n':
            #    conn.sendall(readPacket)

        for writePacket in writeBuf:
            print('output detected', writePacket)
            conn.sendall(writePacket)
        """

        print( '.', end="")

    print('\n--- connection closed in ServerSide thread ---\n')

    # 총 연결수 줄임.
    connection -= 1

    conn.close()
    #exit(1)

def start_server():
    host = '127.0.0.1'
    port = 5000

    global connection   # 연결갯수는 광역변수로.

    # https://aucd29.tistory.com/875    BSD socket BASE.
    # https://on1ystar.github.io/socket%20programming/2021/03/16/socket-1/
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 인터넷 프로토콜 체계 사용, 스트림 방식의 소켓.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # https://learn.microsoft.com/ko-kr/windows/win32/winsock/sol-socket-socket-options
        # 소켓 옵션 지정, 이미 사용중인 주소 및 포트에 바인딩 할수 있도록 선언해줌.
    server_socket.bind((host, port))
        # host, port 지정해서 binding
        # 서버가 미리 생성해 둔 소켓을 ip와 port와 매핑시키는 작업. (외부 클라이언트의 접속을 위해서~~)
    socket.setdefaulttimeout(60)
        # 60초동안 아무짓도 안하면 소켓 연결이 끊김 ...
    print(socket.getdefaulttimeout())

    server_socket.listen(5)
        # 최대 연결 수 5명 지정.

    print('--server Start--')

    while True:
        """
        # 이방식은 소켓 수락이 있을때까지 멈춰 있는 구조임 .... 
        conn, addr = server_socket.accept()
            # conn 은 데이터 주고받기용 연결객체, addr 은 소켓 바인딩 된 주소.
        print('Connected by', addr) # 걍 하나 찍어둡시다...
        threading.Thread(target=client_thread, args=(conn, addr)).start()
            # 접속하면 냅다 thread 생성.
        """

        # 이벤트를 감지해서 진행하는 구조, 루프가 돌고 있는 상태임.
        read_sockets, _, _ = select.select([server_socket], [], [], 3)

        # 주어진 시간동안 데이터가 없으면 (연결이 없으면) 종료되어 버림.... 60 * 3 = 3분.
        if not read_sockets:
            if ( connection <= 0 ) :
                print('연결이 없는 상태에서, 데이터 없이, 주어진 시간이 지남 ... 서버종료.', connection )
                break
            #else:
                #print('.')

        for sock in read_sockets:
            if sock == server_socket:

                conn, addr = server_socket.accept()
                connection += 1
                # conn 은 데이터 주고받기용 연결객체, addr 은 소켓 바인딩 된 주소.
                print('Connected by', addr, 'connection is ', connection )  # 걍 하나 찍어둡시다...
                threading.Thread(target=client_thread, args=(conn, addr)).start()
                # 접속하면 냅다 thread 생성.

                #client_socket, client_address = server.accept()
                #inputs.append(client_socket)

            else:
                data = sock.recv(1024)
                if not data:
                    inputs.remove(sock)
                else:
                    print(data.decode())

    print('--server Ended--' )


if __name__ == '__main__':
    # asyncio.run( start_server() ) # 일케하면 안되지 ... 밑으로 넘어가질 않으니 ....
    threading.Thread(target=start_server).start()

    time.sleep(1)
    print('now client run')
    #start_client()      # thread 가 아니니까 멎어버리는구먼 ..
    #start_client2()
    threading.Thread(target=socClient.start_client, args=('Thread1', ), daemon=True ).start()
    threading.Thread(target=socClient.start_client, args=('Thread2', ), daemon=True ).start()


