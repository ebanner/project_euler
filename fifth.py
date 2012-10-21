total = 0
pdi = []

for num in range(2,1000000):
    string = str(num)
    for char in string:
        total += int(float(char))**5
    if (total == num):
        pdi.append(num)
    total = 0

print(pdi)
