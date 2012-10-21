# generate factoradic numbers (base factorial)
# rightmost digit is base 1, next rightmost is base 1, next rightmost is base
# 2,...
# so let's generate factoradic numbers with 3 digits...

import sys

factoradics = []

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count = 0

for base_10 in range(10):
    for base_9 in range(9):
        for base_8 in range(8):
            for base_7 in range(7):
                for base_6 in range(6):
                    for base_5 in range(5):
                        for base_4 in range(4):
                            for base_3 in range(3):
                                for base_2 in range(2):
                                    for base_1 in range(1):
                                        factoradics.append(str(base_10)+str(base_9)+str(base_8)+str(base_7)+str(base_6)+str(base_5)+str(base_4)+str(base_3)+str(base_2)+str(base_1))
factoradics.sort()
count = 0
permutations = []

for factoradic in factoradics:
    copy_digits = digits[:]
    permute = ''
    for digit in factoradic:
        num = int(float(digit))
        permute += copy_digits[num]
        copy_digits.remove(copy_digits[num])
    permutations.append(permute)
    count += 1
    print("count = {}".format(count))
    if (count == 1000000):
        sys.exit(0)
