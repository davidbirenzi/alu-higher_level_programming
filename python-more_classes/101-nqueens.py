#!/usr/bin/python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:    
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


if __name__ == "__main__":
    main()

