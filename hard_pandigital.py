pandigitals = {}

for i in range(1,100000):
    num = ""
    #print("figuring out {}".format(i))
    possible_num = str(i)
    num += str(possible_num)
    #print(i)
    if int(num[0]) != 9:
        continue
    not_pan = False
    #print(i)
    # check to see if the number is a pandigital itself
    for l in range(len(possible_num)):
        for m in range(l+1,len(possible_num)):
            if possible_num[l] == possible_num[m]:
                #print("{} itself is not a pandigital!".format(possible_num))
                not_pan = True
                break
    if not_pan:
        continue
    for j in range(2,10):
        #print(num)
        #print("i*j={0}*{1}".format(i,j))
        #print("possible num is {}".format(possible_num))
        possible_num = str(i*j)
        #print("possible num = {0}*{1} = {2}".format(i,j,possible_num))

        if len(num) == 9:
            # it's now or never to add num
            #print("{} is a pandigital".format(num))
            #if int(num) > MAX:
                #MAX = int(num)
            pandigitals[i] = num
            break

        elif len(num+possible_num) > 9:
            #print("adding {0} to {1} would put us over 9".format(possible_num,num))
            break

        # check to see if the number is a pandigital itself
        for l in range(len(possible_num)):
            for m in range(l+1,len(possible_num)):
                if possible_num[l] == possible_num[m]:
                    #print("{} itself is not a pandigital!".format(possible_num))
                    not_pan = True
        if not_pan:
            break

        for k,digit in enumerate(possible_num):
            # check to see if we can add the new digit
            #print("does {0} contain {1}?".format(num,digit))
            if num.__contains__(digit):
                #print("{0} already contains {1} -- throwing it away".format(num,digit))
                #print("yes")
                not_pan = True
                break
            #print("no")
        if not_pan:
            #print("not a pandigital, duplicate digits")
            break
        # we got all the way down here, so it must be OK to add the next number
        num += possible_num

print(pandigitals)
