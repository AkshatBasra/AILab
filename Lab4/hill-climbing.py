import random

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(' '.join(row))
    print()

def compute_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_best_neighbor(board):
    n = len(board)
    current_conflicts = compute_conflicts(board)
    best_board = board[:]
    best_conflicts = current_conflicts


    for i in range(n):
        for j in range(i + 1, n):
            new_board = board[:]
            new_board[i], new_board[j] = new_board[j], new_board[i]
            new_conflicts = compute_conflicts(new_board)
            if new_conflicts < best_conflicts:
                best_conflicts = new_conflicts
                best_board = new_board[:]

    return best_board, best_conflicts

def hill_climbing(n):
    board = random.sample(range(n), n)
    print(f"Initial board: {board}, Cost = {compute_conflicts(board)}\n")
    sideways_moves = 0
    max_sides = 2

    while True:
        print(f"{board} -> Cost = {compute_conflicts(board)}")
        neighbor, neighbor_conflicts = get_best_neighbor(board)

        current_conflicts = compute_conflicts(board)
        if neighbor_conflicts < current_conflicts:
            board = neighbor
            sideways_moves = 0
        elif neighbor_conflicts == current_conflicts and sideways_moves < max_sides:
            print(f"Sideways here: {sideways_moves}")
            board = neighbor
            sideways_moves += 1
        else:
            break
        if neighbor_conflicts == 0:
            print("\nGoal state reached!")
            print_board(board)
            return
    print("\nNo solution found from this start.")

hill_climbing(4)
