import random

def print_board(board):
    """Display the board in a readable 4x4 format."""
    n = len(board)
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(' '.join(row))
    print()

def compute_conflicts(board):
    """Return the total number of pairs of queens attacking each other."""
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_best_neighbor(board):
    """Return the best neighbor and its conflict count."""
    n = len(board)
    current_conflicts = compute_conflicts(board)
    best_board = board[:]
    best_conflicts = current_conflicts

    print(f"\nCurrent board: {board}, Cost = {current_conflicts}")
    print_board(board)
    print("Neighbor boards with their costs:")

    for row in range(n):
        for col in range(n):
            if col == board[row]:
                continue
            new_board = board[:]
            new_board[row] = col
            new_conflicts = compute_conflicts(new_board)
            print(f"{new_board} -> Cost = {new_conflicts}")
            if new_conflicts < best_conflicts:
                best_conflicts = new_conflicts
                best_board = new_board[:]

    return best_board, best_conflicts

def hill_climbing_4queens():
    n = 4
    board = [random.randint(0, n - 1) for _ in range(n)]
    print(f"Initial board: {board}, Cost = {compute_conflicts(board)}\n")

    while True:
        neighbor, neighbor_conflicts = get_best_neighbor(board)
        if neighbor_conflicts >= compute_conflicts(board):
            # No better neighbor — local maximum reached
            print("\nReached local optimum.")
            break
        board = neighbor
        if neighbor_conflicts == 0:
            print("\n✅ Goal state reached!")
            print_board(board)
            return
    print("\n❌ No solution found from this start.")

if __name__ == "__main__":
    hill_climbing_4queens()
