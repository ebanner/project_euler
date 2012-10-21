def moves(m,n):
    if (m == 0):
        return n
    elif (n == 0):
        return m
    else:
        return moves(m-1,n) + moves(m,n-1)
