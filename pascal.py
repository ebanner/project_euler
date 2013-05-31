if __name__ == '__main__':
    grid = [0]*21

    for i in range(21):
        grid[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(21):
        grid[0][i] = 1
        grid[i][0] = 1

    for i in range(1,21):
        for j in range(1,21):
            grid[i][j] = grid[i][j-1] + grid[i-1][j]

    for i in range(21):
        for j in range(21):
            print("%6i" % grid[i][j], end=" ")
        print()
