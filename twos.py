def sum_the_digits(string):
    total = 0
    string = str(string)
    for char in string:
        total += int(float(char))
    return total

#for i in range(40):
#    sum_digits = sum_the_digits(2**i)
#
#    print("2**%2d = %6d = %d" % (i, 2**i, sum_digits))

print(sum_the_digits(2**1000))
