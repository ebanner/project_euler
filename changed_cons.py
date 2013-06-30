import sys
from Euler import short_prime_factors

cons = [0]*4

if __name__ == '__main__':
    for n in range(1,1000000):
        answer = True
        print(n)

        for i in range(len(cons)):
            cons[i] = short_prime_factors(n+i)
            if len(cons[i]) != 4:
                answer = False

        if not answer:
            continue

        if not answer:
            break

        print("the first four consecutive digits are")
        for i in range(len(cons)):
            print(n+i, end=' ')
        print()
        sys.exit(0)
