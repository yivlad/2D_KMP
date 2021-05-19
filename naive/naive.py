class NaiveSearch:
    def _check(self, M, P, i, j):
        for x in range(len(P)):
            for y in range(len(P[x])):
                if M[i + x][j + y] != P[x][y]:
                    return False

        return True

    def find(self, M, P):
        matches_ij = []

        for i in range(len(M) - len(P) + 1):
            for j in range(len(M[0]) - len(P[0]) + 1):
                if self._check(M, P, i, j):
                    matches_ij.append((i + 1, j + 1))

        return matches_ij