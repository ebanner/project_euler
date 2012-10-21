f = open('words.txt', 'r')

words = f.read()
words = words.split('","')
words[0],words[-1] = words[0].lstrip('"'),words[-1].rstrip('"')
print(words)
values = [0]*len(words)

# 364 is the max word value of a word
max_length = 0

#for word in words:
#    if len(word) > max_length:
#        max_length = len(word)
#print(max_length)

# compute the value of each word
for i,word in enumerate(words):
    word_value = 0
    for char in word:
        word_value += ord(char)-64
    values[i] = word_value

print(values)

triangle_words = []

for i,T in enumerate(values):
    n = 1
    while (n*(n+1) <= 2*T):
        if n*(n+1) == 2*T:
            triangle_words.append(words[i])
            break
        n += 1

print("there are {} triangle words".format(len(triangle_words)))
