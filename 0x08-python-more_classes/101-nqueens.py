#!/usr/bin/python3
import sys


def get_N():
    """ get_N - a function that ckeck argv and error and
        Return (N: int): The size of Classboard
    """
    N = 0
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


class Queen:
    def __init__(self, N):
        self.N = N  # The size of board
        self.board = [[0 for i in range(N)] for j in range(N)]
        self.solution = []

    def is_safe(self, row, col):
        # check if they are in the same row
        for i in range(self.N):
            if self.board[row][i] == 1:
                return False

        # check the upper left diagonal:
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # check the upper right digonal:
        i = row - 1
        j = col + 1
        while i >= 0 and j < self.N:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        # check the the lower left diagonal
        i = row + 1
        j = col - 1
        while i < self.N and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        # check the lower right diagonal
        i = row + 1
        j = col + 1
        while i < self.N and j < self.N:
            if self.board[i][j] == 1:
                return False
            i += 1
            j += 1
        return True

    def solve(self, col=0):
        if col == self.N:
            sol = []
            for i in range(self.N):
                for j in range(self.N):
                    if self.board[i][j] == 1:
                        sol.append([i, j])
            self.solution.append(sol)
            return

        for row in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(col + 1)
                self.board[row][col] = 0

    def __str__(self):
        ret = ""
        for a in range(len(self.solution)):
            ret += str(self.solution[a]) + "\n"
        return ret[:-1]


if __name__ == '__main__':
    N = get_N()
    position_of_all_queen = Queen(N)
    position_of_all_queen.solve()
    print(position_of_all_queen)
