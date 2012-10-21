f = open('numbers.txt', 'r')

numbers = f.readlines()
numbers = map(lambda line: line.strip('\n'), numbers)
numbers = [number for number in numbers]

sum = 0

for i in range(len(numbers)):
    sum += int(float(numbers[i]))

print(str(sum)[0:10])
