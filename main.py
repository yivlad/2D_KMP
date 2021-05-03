from aho_corasick import Automaton

M = []
P = []

with open('example.txt', 'r') as file:
    sizes = file.readline().split()
    m = int(sizes[0])
    n = int(sizes[1])
    a = int(sizes[2])
    b = int(sizes[3])
    for _ in range(m):
        M.append(file.readline().split())
    for _ in range(a):
        P.append(file.readline().split())

automaton = Automaton()
print(automaton.build(list(map(list, zip(*P)))))
Mp = [[-1] * len(M[i]) for i in range(len(M))]

for i in range(len(M[0])):
    automaton.reset()
    for j in range(len(M)):
        automaton.go(M[j][i])
        Mp[j][i] = automaton.state.num

print("\n".join(["".join(map(str, row)) for row in Mp]))