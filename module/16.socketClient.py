import socket
import time
import threading
# import msvcrt   # Microsoft 계열에서.. 사용하는 crt 처리. 리눅스 안먹힘...
                # https://whitewing4139.tistory.com/165
                # 안쓰고 푸는게 좋음.. (종속되지 않게...)
import queue    # queue 를 사용해서 쓰레드 관리.
# event를 사용한 관리방법, https://superfastpython.com/thread-event-object-in-python/
# import select
# import sys

"""
about thread 
    - https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
        - 직접적인 thread 종료하는 방법을 python 은 제공하지 않음. 
    - https://stackoverflow.com/questions/39501529/python-stop-thread-with-raw-input
        - input 대기 상태에서 종료하는 방법.
"""

q = queue.Queue()

# ansi color 지정 .. 플랫폼마다 틀림 ...
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print2( *args, **kwargs ):
    print( "\n\t", end="" )
    print( *args, **kwargs )

def client_send(conn: socket, thread_name: str, q : queue.Queue ):
    print2('client_send() run')
    try :
        #while True:
        while conn:

            #msg = raw_input('\nMe > ')
            data = input(f'{thread_name} Send Message > ')
                # input 으로 받으면 프로세스가 멈춰있는 상태 ..
                # 즉, 다른 thread 가 뻗어도, 뭔가 체크할 방법이 없다. 
            conn.send(data.encode('utf-8'))
            #print( type(data), data )
            if data == 'bye':
                print2(f'{thread_name} disconnected')
                break


            """
            if msvcrt.kbhit():
            key = msvcrt.getch()
            print(f"Key pressed: {key}")
            conn.send( key )
            """

            """ ... 얘도 안되네 ..
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                print('select event occurred')
                user_input = input("Enter something: ")
                print(f"You entered: {user_input}")

            print('.', end="")
            """

    except Exception as err:
        print2( f'{thread_name} conn is invalid in client_send')
        print2( err )
        raise Exception(f'{thread_name} Exception in client_send')

    print2(f'{thread_name} writer exited !!')

def client_receive(conn: socket, thread_name: str, q : queue.Queue ):
    print2('client_receive() run')
    try :
        while True:
            data = conn.recv(1024)
            data_encode = str(data, 'utf-8')

            if not data:
                break
            elif data_encode == 'Connection Finished':
                break

            print2(f'{thread_name} listener RCV packet :', str(data))
            #print(type(data_encode), data_encode)
    except Exception as err:
        print2(f'{thread_name} conn is invalid in client_receive')
        print2(err)
        raise Exception(f'{thread_name} Exception in client_receive')

    print2( f'{thread_name} listener exited !!')
    q.put('fin')

def custom_hook(args) :
    print2( f'Exception is occurred - {args.exc_value}')

    global q
    q.put('fin')

def start_client( thread_name ):
    host = '127.0.0.1'
    port = 5000

    global q

    print2(f'--client start - {thread_name} --')

    """
    print2( type(q) )
    q.put('hello')
    print2( q.qsize() )
    print2( q.get() )
    exit(1)
    """

    #threading.excepthook = custom_hook    # thread exception 발생시 이리로 ...
        # 오류 처리는 피할 수 있지만 ...
        # 오류를 정확히 파악하기는 힘들어지는 상황이 된다.
    threads = []

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try :
        # send 용 Thread 하나, receive 용 Thread 하나 생성해서 둘 다 동시에 처리할 수 있도록 한다.
        t1 = threading.Thread(target=client_send, args=(client_socket, thread_name, q), daemon=True)
        t1.start()
        threads.append(t1)

        # 아래처럼 바로 대입은 안된다. 안된다
        # t2 = threading.Thread(target=client_receive, args=(client_socket,)).start()
        # threads.append(t2)
        # 얘도 안된다.
        # threads.append( threading.Thread(target=client_receive, args=(client_socket,)).start() )

        t2 = threading.Thread(target=client_receive, args=(client_socket, thread_name, q), daemon=True)
            # 파라메터 한개일땐 반드시 (aaa, )
        t2.start()
        threads.append(t2)

        print2('thread list is', threads)

        time.sleep(3);
    except :
        # exception 으로 감지되지 않음 ...
        print2('Exception 발생 ... ' + thread_name )

    """
    while True:
        if q.qsize() > 0:
            q_cmd = q.get()
            if q_cmd == 'fin':
                print2('queue value is FIN')
                break
    """

    #while 에서 체크되면 바로 종료 ...
    for t in threads:
        t.join()  # join으로 스레드가 종료될때까지 기다린다.

    client_socket.close()   # 서버에서 끊어버렸는데 ... ???
    print2(bcolors.WARNING + f'\nclient thread {thread_name} exited\n' + bcolors.ENDC )


if __name__ == '__main__':
    threading.Thread(target=start_client, args=('Thread1', ), daemon=True).start()
    time.sleep(2)
