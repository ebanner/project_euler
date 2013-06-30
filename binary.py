if __name__ == '__main__':
    f = open('triangle.txt', 'r')
    lines = f.readlines()

    lines = map(lambda line: line.strip('\n'), lines)
    lines = [line for line in lines]

    array = []

    for line in lines:
        array.append([line])

    tree = []

    for element in range(len(array)):
        tree.append(array[element][0].split())

    for i in range(len(tree)):
        for j in range(len(tree[i])):
            print(tree[i][j], end=" ")
            tree[i][j] = int(float(tree[i][j]))
        print()

