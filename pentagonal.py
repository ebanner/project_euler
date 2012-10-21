import sys

#def is_pentagonal(P):
    #n = 1
    #while n*(3*n-1) < 2*P:
    #    n += 1
    #if n*(3*n-1) == 2*P:
    #    return True
    #else:
    #    return False

pentagonals = []

for n in range(1,10000+1):
    pentagonals.append(n*(3*n-1)//2)

for i,P1 in enumerate(pentagonals):
    print(i)
    for j in range(i+1,len(pentagonals)):
        P2 = pentagonals[j]
        P_sum,P_diff = P1+P2,abs(P1-P2)
        if pentagonals.__contains__(P_sum) and pentagonals.__contains__(P_diff):
            print("sum and difference of {0} and {1} are pentagonal!".format(P1,P2))
            sys.exit(0)
