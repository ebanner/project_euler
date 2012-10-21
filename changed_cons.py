import sys
from Euler import short_prime_factors

cons = [0]*4

for n in range(1,1000000):
    answer = True
    print(n)

    for i in range(len(cons)):
        cons[i] = short_prime_factors(n+i)
        if len(cons[i]) != 4:
            answer = False

    if not answer:
        continue

#    for i in range(4):
#        if not answer:
#            break
#        for j in range(4):
#            if cons[0][i] == cons[1][j] or cons[0][i] == cons[2][j] or cons[0][i] == cons[3][j] or cons[1][i] == cons[2][j] or cons[1][i] == cons[3][j] or cons[2][i] == cons[3][j]:
#                answer = False
#                break

    if not answer:
        break

    print("the first four consecutive digits are")
    for i in range(len(cons)):
        print(n+i, end=' ')
    print()
    sys.exit(0)
