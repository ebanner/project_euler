#def collatz(n, count, checked):  # start count at 1
#    if (n == 1):  # we're done
#        #print("--> {}".format(n))
#        #print("count: {}".format(count))
#        return count
#    elif (n % 2 == 0):  # n is even
#        #print("--> {}".format(n), end=" ")
#        checked[n] = True
#        return collatz(int(n/2),count+1,checked)
#    else:  # n is odd and not 1
#        #print("--> {}".format(n), end=" ")
#        checked[n] = True
#        return collatz(3*n+1,count+1,checked)

def collatz(n, count):
    while (n != 1):
        count += 1
        if (n % 2 == 0):  # n is even
            #print("--> {}".format(n), end=" ")
            n = int(n/2)
        else:
            #print("--> {}".format(n), end=" ")
            n = 3*n+1
        #checked[n] = True
    #print("--> {}".format(n))
    #print("count: {}".format(count))

    return count

NUM = 1000000
max_count = 0
#checked = [False]*100000000

for num in range(1,NUM):
    if (num % 1000 == 0):
        print("num = {}".format(num))
    #if (checked[num]):
    #    continue
    count = collatz(num, 1)
    if (count > max_count):
        max_count = count
        longest_chain = [max_count, num]
