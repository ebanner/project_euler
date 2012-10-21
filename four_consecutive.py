import sys
from Euler import prime_factors

f1,f2,f3,f4 = prime_factors(1),prime_factors(2),prime_factors(3),prime_factors(4)

for n in range(5,1000000):
    #answer = True

    if n % 1000 == 0:
        print(n)

    # slide the factors down
    #f1 = f2[:]
    #f2 = f3[:]
    #f3 = f4[:]
    f4 = prime_factors(n)

    #print(n)

    #for f in f1:
    #    if f2.__contains__(f) or f3.__contains__(f) or f4.__contains__(f):
    #        answer = False
    #        break

    #if not answer:
    #    continue
    #
    #for f in f2:
    #    if f3.__contains__(f) or f4.__contains__(f):
    #        answer = False
    #        break

    #if not answer:
    #    continue

    #for f in f3:
    #    if f4.__contains__(f):
    #        answer = False
    #        break

    #if not answer:
    #    continue

    #print("the first four consecutive digits are")
    #for i in range(len(cons)):
    #    print(n+i, end=' ')
    #print()
    #sys.exit(0)
