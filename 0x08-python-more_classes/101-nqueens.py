#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard """
import sys


class NQueen:
    """ N queen class"""
    def __init__(self, y):
        """ Global vars """
        self.y = y
        self.x = [0 for i in range(y + 1)]
        self.result = []

    def place(self, k, i):
        """ queen can be in i(True)
        or if the are attacking queens in row or diagonal (False)
        """
        for j in range(1, k):
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """ every queen on board

        Args:

        k: queen to evaluate
        """
        for i in range(1, self.y + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.y:
                    solution = []
                    for i in range(1, self.y + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.result.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.result

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
result = queen.nQueen(1)

for i in result:
    print(i)
