import socket
import selectors
import random
import threading
import time
import sys

# 정상적인 파일 이름이 아닌 dot(.)이 들어간 파일 라이브러리는 import 과정이 복잡해진다.
import importlib.util
spec = importlib.util.spec_from_file_location(
    name="socClient",  # note that ".test" is not a valid module name
    location="./module/16.socketClient.py",
)
socClient = importlib.util.module_from_spec(spec)
spec.loader.exec_module(socClient)
# 위 플로우를 통하여 socClient 에 module 을 로드함.

# selector 는 맨 앞에 상단에서 선언되어야 함 ... 함수 내부에서도 호출됨.
sel = selectors.DefaultSelector()
connection = 0

import sys                      # subdirectory 의 module 을 땡기기 위해선,
sys.path.append("./module")     # sys 로딩하고 모듈 path에 디렉토리를 넣어줘야
import Strikers                 # 그제서야 땡길 수 있다.

def accept_client(sock):
    global sel
    global connection

    """ 서버 소켓에 클라이언트가 접속하면 호출된다. """
    conn, addr = sock.accept()
    sel.register(conn, selectors.EVENT_READ, game_client)
        # 소켓에 데이터를 수신하면 game_client() 함수가 실행되도록 설정
    connection += 1
    print( '\n--- client connection occurred', conn, connection, "---\n", flush=True)
    conn.sendall(b'game started')

def game_client(conn):
    try:
        global connection

        strikers = Strikers.Strikers()
        strikers.init()

        while True:
            data = conn.recv(1024)
            #print('Received data Type / data From Client : ', type(data), data, str(data, 'utf-8'), flush=True)
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
            else:
                strike, ball, out = strikers.check(data_encode)
                count = strikers.getCount()

                if strike == 3:
                    finish_str = 'Finished - ' + str(strikers.rtn()) + ' and NewGame Started'
                    strikers.init()
                else:
                    finish_str = f'Strike : {strike} Ball :{ball} Out :{out} Count :{count}'

                conn.sendall(finish_str.encode('utf-8'))

    except Exception as err:
        print('Exception in server game_client')
        print(err)

    print('\n--- connection closed in ServerSide thread ---\n')

    # 총 연결수 줄임.
    connection -= 1

    conn.close()


def start_server():
    host = '127.0.0.1'
    port = 5000

    global connection   # 연결갯수는 광역변수로.
    global sel

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
    #print(socket.getdefaulttimeout())

    server_socket.listen(5)
        # 최대 연결 수 5명 지정.

    print('--server Start--')
    sel.register(server_socket, selectors.EVENT_READ, accept_client)  # 연결시 실행될 함수 등록.

    while True:
        events = sel.select( timeout=1 )  # 클라이언트의 접속 또는 접속된 클라이언트의 데이터 요청을 감시

        # 주어진 시간동안 데이터가 없으면 (연결이 없으면) 종료되어 버림.... 60 * 3 = 3분.
        if not events:
            if ( connection <= 0 ) :
                print('연결이 없는 상태에서, 데이터 없이, 주어진 시간이 지남 ... 서버종료.', connection, flush=True )
                break
        else:
            for key, mask in events:
                # print( '@@@event')
                # print( 'key is', key)
                # print( 'mask is', mask )
                # print( '@@@@')
                callback = key.data  # 실행할 함수
                callback(key.fileobj)  # 이벤트가 발생한 소켓을 인수로 실행할 함수를 실행한다.

    print('--server Ended--' )


if __name__ == '__main__':
    sys.stdout.flush()
    threading.Thread(target=start_server).start()

    time.sleep(1)
    print('-- now client run --', flush=True)
    threading.Thread(target=socClient.start_client, args=('Thread1', ), daemon=True ).start()
    threading.Thread(target=socClient.start_client, args=('Thread2',), daemon=True).start()
