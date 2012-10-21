def is_pandigital(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] == num[j]:
                return False
    return True

pandigitals = []

for num in range(9000,9999):
    string_num = ""
    n = 1
    while (len(string_num) < 9):
        string_num += str(num*n)
        n += 1
    if len(string_num) == 9 and is_pandigital(string_num) and not string_num.__contains__('0'):
        print("{}".format(num))
        print("{} is a pandigital!".format(string_num))
        pandigitals.append(int(string_num))
    else:
        #print("{} has more than nine digits -- throw it away!".format(string_num))
        pass
