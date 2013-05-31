def right_pad(num, length):
    if (length == 0):
        return num
    else:
        num += '0'
        return right_pad(num, length-1)

def reverse(string):
    temp = ""
    for i in range(len(string)):
        temp += string[len(string)-1-i]
    return temp

def pal_huh(string):
    if (len(string) == 0 or len(string) == 1):
        return True
    elif (string[0] == string[-1]):
        return pal_huh(string[1:-1])
    else:
        return False

if __name__ == '__main__':
    total = 0

    for i in range(2**10):
        b = bin(i)[2:]
        b = reverse(str(b))
        left = right_pad(b,10-len(b))
        right = "{:010b}".format(i)

        num_10 = int(left+right,2)
        if (num_10 == 585):
            print(num_10)
        if (num_10 < 1000000 and pal_huh(str(num_10))):
            total += num_10
            print(num_10)
