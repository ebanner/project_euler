def fib(n, a, b):
    while (n > 1):
        a,b = b,a+b
        n -= 1
    return a

def fibonacci(n):
    return fib(n, 1, 1)

if __name__ == '__main__':
    n = 1

    while (len(str(fibonacci(n))) != 1000):
        n += 1
