if __name__ == '__main__':
    f = open('grid.txt', 'r')
    lines = f.readlines()

    lines = map(lambda line: line.strip('\n'), lines)
    lines = [line for line in lines]

    # okay, so all of the lines are in a 1-d array... let's get them into a 2-d
    # array

    array = []

    for line in lines:
        array.append([line])

    matrix = []

    for element in range(len(array)):
        matrix.append(array[element][0].split())

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
            matrix[i][j] = int(float(matrix[i][j]))
        print()

    # matrix is now a 2-d array that contains all elements in the grid of numbers
    # now what's our gameplan?
    # let's go left to right first

    max_val = curr_val = 0

    print("checking horizontal")
    for i in range(len(matrix)):
        for j in range(len(matrix)-4):
            curr_val = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
            if (curr_val > max_val):
                max_val = curr_val
                print("new max val: {0} * {1} * {2} * {3} = {4}".format(matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i][j+3], max_val))

    # so we have the great product along the horizontal in max_val
    # do the same thing for vertically

    print("checking vertical")
    for j in range(len(matrix[j])):
        for i in range(len(matrix)-4):
            curr_val = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
            if (curr_val > max_val):
                max_val = curr_val
                print("new max val: {0} * {1} * {2} * {3} = {4}".format(matrix[i][j], matrix[i+1][j], matrix[i+2][j], matrix[i+3][j], max_val))

    print("checking diagonally northwest to southeast")
    for i in range(len(matrix[j])-4):
        for j in range(len(matrix)-4):
            curr_val = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
            if (curr_val > max_val):
                max_val = curr_val
                print("new max val: {0} * {1} * {2} * {3} = {4}".format(matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3], max_val))


    print("checking diagonally northeast to southwest")
    for i in range(len(matrix[j])-4):
        for j in range(4, len(matrix)):
            curr_val = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3]
            if (curr_val > max_val):
                max_val = curr_val
                print("new max val: {0} * {1} * {2} * {3} = {4}".format(matrix[i][j], matrix[i+1][j-1], matrix[i+2][j-2], matrix[i+3][j-3], max_val))
