
import random 

class Strikers:
    def __init__(self):  # constructor
        self.init()

    def init(self):
        self.count = 1
        base = [vars for vars in range(1, 10)]
        random.shuffle(base)
        self.arr = [base[0], base[1], base[2]]

    # return strike, ball, out.
    def _match_check(self, onenum: int, loc: int):
        # print('onenum is ', onenum)
        if onenum in self.arr:
            if onenum == self.arr[loc]:
                return 1, 0, 0
            else:
                return 0, 1, 0
        return 0, 0, 1

    def check(self, countstr):
        self.count += 1
        strike, ball, out = 0, 0, 0

        # print(type(countstr))
        # print(len(countstr))
        # print(countstr.isdigit())
        # print(countstr)

        if countstr.isdigit() and len(countstr) == 3:
            for i in range(0, 3):
                s, b, o = self._match_check(int(countstr[i]), i)
                strike += s
                ball += b
                out += o

            return strike, ball, out

        return 0, 0, 1

    def getCount(self):
        return self.count

    def rtn(self):
        return self.arr


if __name__ == '__main__':
    # console case ... 
    strikers = Strikers()
    strikers.init()
    while True:
        getStr = input('input num3 : ')
        strike, ball, out = strikers.check(getStr)
        print( 'Strike :', strike, ' Ball :', ball, ' Out :', out, ' Count :', strikers.getCount() )
        if strike == 3:
            break
    print('fin')
