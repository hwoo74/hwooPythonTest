import socketserver
import threading
import time

# 정상적인 파일 이름이 아닌 dot(.)이 들어간 파일 라이브러리는 import 과정이 복잡해진다.
import importlib.util

spec = importlib.util.spec_from_file_location(
    name="socClient",  # note that ".test" is not a valid module name
    location="./module/16.socketClient.py",
)
socClient = importlib.util.module_from_spec(spec)
spec.loader.exec_module(socClient)
# 위 플로우를 통하여 socClient 에 module 을 로드함.


import sys                      # subdirectory 의 module 을 땡기기 위해선,
sys.path.append("./module")     # sys 로딩하고 모듈 path에 디렉토리를 넣어줘야
import Strikers                 # 그제서야 땡길 수 있다.

connection = 0

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        try :
            global connection

            """ 서버 소켓에 클라이언트가 접속하면 호출된다. """
            connection += 1
            print('\n--- client connection occurred', connection, "---\n", flush=True)
            self.request.sendall(b'game started')

            strikers = Strikers.Strikers()
            strikers.init()

            while True:
                data = self.request.recv(1024)
                # print('Received data Type / data From Client : ', type(data), data, str(data, 'utf-8'), flush=True)
                data_encode = str(data, 'utf-8')

                if not data:
                    break
                elif data_encode == '':
                    self.request.sendall('data is null'.encode('utf-8'))
                elif data_encode == 'bye':
                    self.request.sendall('Connection Finished'.encode('utf-8'))
                    print('client disconnected')
                    break
                elif data_encode == 'hello':
                    self.request.sendall('Hi'.encode('utf-8'))
                else:
                    strike, ball, out = strikers.check(data_encode)
                    count = strikers.getCount()

                    if strike == 3:
                        finish_str = 'Finished - ' + str(strikers.rtn()) + ' and NewGame Started'
                        strikers.init()
                    else:
                        finish_str = f'Strike : {strike} Ball :{ball} Out :{out} Count :{count}'

                    self.request.sendall(finish_str.encode('utf-8'))

        except Exception as err:
            print('Exception in server handle')
            print(err)

        print('\n--- connection closed in ServerSide thread ---\n')

        # 총 연결수 줄임.
        connection -= 1


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def socketServer() :
    host, port = '127.0.0.1', 5000
    with ThreadedTCPServer((host, port), MyTCPHandler) as server:
        server.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=socketServer).start()

    time.sleep(1)
    print('-- now client run --', flush=True)
    threading.Thread(target=socClient.start_client, args=('Thread1',), daemon=True).start()
    threading.Thread(target=socClient.start_client, args=('Thread2',), daemon=True).start()
