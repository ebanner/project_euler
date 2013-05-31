if __name__ == '__main__':
    pandigitals = {}

    for i in range(1,100000):
        num = ""
        possible_num = str(i)
        num += str(possible_num)
        if int(num[0]) != 9:
            continue
        not_pan = False
        # check to see if the number is a pandigital itself
        for l in range(len(possible_num)):
            for m in range(l+1,len(possible_num)):
                if possible_num[l] == possible_num[m]:
                    not_pan = True
                    break
        if not_pan:
            continue
        for j in range(2,10):
            possible_num = str(i*j)

            if len(num) == 9:
                # it's now or never to add num
                pandigitals[i] = num
                break

            elif len(num+possible_num) > 9:
                break

            # check to see if the number is a pandigital itself
            for l in range(len(possible_num)):
                for m in range(l+1,len(possible_num)):
                    if possible_num[l] == possible_num[m]:
                        not_pan = True
            if not_pan:
                break

            for k,digit in enumerate(possible_num):
                # check to see if we can add the new digit
                if num.__contains__(digit):
                    not_pan = True
                    break
            if not_pan:
                break
            # we got all the way down here, so it must be OK to add the next number
            num += possible_num

    print(pandigitals)
