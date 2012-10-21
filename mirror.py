def pal_huh(string):
    if (len(string) == 0 or len(string) == 1):
        return True
    elif (string[0] == string[-1]):
        return pal_huh(string[1:-1])
    else:
        return False

total = 0

for i in range(0,1000000):
    if (pal_huh(str(i)) and pal_huh(bin(i)[2:])):
        print("{0} and {1} are palindromic".format(i, bin(i)[2:]))
        total += i
