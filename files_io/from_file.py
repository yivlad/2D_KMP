def from_file(filename):
    M = []
    P = []

    with open(filename, 'r') as file:
        sizes = file.readline().split()
        m = int(sizes[0])
        n = int(sizes[1])
        a = int(sizes[2])
        b = int(sizes[3])
        for _ in range(m):
            M.append([int(symbol) for symbol in file.readline().split()])
        for _ in range(a):
            P.append([int(symbol) for symbol in file.readline().split()])

    return M, P
