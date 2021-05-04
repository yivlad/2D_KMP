from aho_corasick import Automaton
from knuth_morris_pratt import Pattern

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
column_end_states = automaton.build(list(map(list, zip(*P))))
Mp = [[-1] * len(M[i]) for i in range(len(M))]

for i in range(len(M[0])):
    automaton.reset()
    for j in range(len(M)):
        automaton.go(M[j][i])
        Mp[j][i] = automaton.state.num

kmp_pattern = Pattern(column_end_states)
matches_ij = []
for j, row in enumerate(Mp):
    matches_in_row = kmp_pattern.find_matches(row)
    for match_i in matches_in_row:
        j_in_M = j - a + 1  # current j is the last row of a match and we want its first row
        matches_ij.append((j_in_M + 1, match_i + 1))  # we add 1 to i and j for one based indexing

with open("output.txt", "w") as file:
    file.write(f"{len(matches_ij)}\n")
    file.writelines([f"{i} {j}\n" for (i, j) in matches_ij])
