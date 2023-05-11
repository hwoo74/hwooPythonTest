import os
import sys                      # subdirectory 의 module 을 땡기기 위해선,
sys.path.append("./module")     # sys 로딩하고 모듈 path에 디렉토리를 넣어줘야
from Strikers import Strikers   # 간단히 땡기쟈.

import cmd
# https://docs.python.org/ko/3.7/library/cmd.html
# pycharm 에서는 화살표 키가 먹히나, 실 콘솔에서는 안먹힘... 궂이 막을 필요 없음 ;;;

import atexit

def handle_exit():
    #print("프로그램 종료시 반드시 호출되는 함수.. ")
    #print("Exception 발생으로 인한 종료에도 호출됨.")
    #print("Ctrl-C 일때도 호출됨.")
    print("종료되었습니다.")

atexit.register(handle_exit)    # handle_exit() 함수를 프로그램 종료 시 호출하도록 등록


import traceback
# Exception 발생시 정확한 위치를 추적한다.
# print(traceback.format_exc())

class CmdTest(cmd.Cmd):
    intro = 'match distinct 3 number. it\'s cmd Test game.\n ? is help'
    prompt = 'input 3 number (1~9) : '

    def preloop(self):
        # 이벤트 루프가 시작되기 전에 돌아가는 함수임 .
        self.strikers = Strikers()

    def do_test(self, *args):
        """ ? test 하면 이 내용이 출력됩니다. 즉, 도움말 출력을 위한 주석 부분. """
        print('do 다음에 적어놓은 이름으로 바로 적용되는 함수.')
        print('do_test(self, *args) 같은 식으로 선언... 반드시 파라메터 받아야 함.')
        print('자동으로 도움말 help or ? 에도 추가됨.')
    def do_quit(self, *args):
        """ 게임종료 """
        print('Finish')
        return True

    def do_exit(self, *args):
        """ 얘도 종료 함수 """
        return self.do_quit()

    def do_error(self, *args):
        """ 강제로 Exception 을 발생시킴 """
        raise Exception('test exception')

    def emptyline(self, *args):
        # 암것도 입력 안했을때 돌아감 ..
        print('뭐라도 입력하세요..')

    def default(self, *args):
        # 함수가 없으면 얘가 돌아감.
        # print( '기본함수 돌아간다', args[0], *args)
        count = self.strikers.getCount()
        strike, ball, out = self.strikers.check(args[0])
        print('Strike :', strike, ' Ball :', ball, ' Out :', out, ' Count :', count)
        if strike == 3:
            print( 'Finished. Result is ', self.strikers.rtn(), ' count is ', count )
            print( 'NewGame inited')
            self.strikers.init()

"""
tGame = CmdTest()
tGame.cmdloop()
"""

try :
    tGame = CmdTest()
    tGame.cmdloop()
except Exception as err:                     # 정의되지 않은 오류.
    print('exception occurred.')
    print( err )
    print( '-' * 20 )
    print(traceback.format_exc())