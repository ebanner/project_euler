def sum_the_digits(string):
    total = 0
    string = str(string)
    for char in string:
        total += int(float(char))
    return total

if __name__ == '__main__':
    print(sum_the_digits(2**1000))
