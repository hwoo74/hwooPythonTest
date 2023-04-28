PI = 3.14159265358979323846
ROOT1 = 1.414213
ROOT2 = 1.732050

def fibonacci(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

class Factoria:
    def get(self, num):
        res = 1
        for vars in range(2, abs(num) + 1) :
            res *= vars
        if num < 0:
            res *= -1
        return res

if __name__ == "__main__":
    print( fibonacci(-1) )
    print( fibonacci(0) )
    print( fibonacci(1) )
    print( fibonacci(2) )
    print( fibonacci(3) )

    fa = Factoria();
    print( fa.get(-3) );
