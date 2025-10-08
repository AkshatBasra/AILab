import random, math

def print_board(board):
    """Display the board in a readable 4x4 format."""
    n = len(board)
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(' '.join(row))
    print()

def cost(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                conflicts += 1
    return conflicts

def random_neighbor(state):
    n = len(state)
    new_state = state[:]
    col = random.randint(0, n-1)
    new_row = random.randint(0, n-1)
    while new_row == new_state[col]:
        new_row = random.randint(0, n-1)
    new_state[col] = new_row
    return new_state

def simulated_annealing(n, T=1.0, k=0.999):
    state = [random.randint(0, n-1) for _ in range(n)]
    print("Initial State:")
    print_board(state)
    while True:
        if cost(state) == 0:
            return state
        neighbor = random_neighbor(state)
        delta = cost(neighbor) - cost(state)

        if delta < 0 or random.random() < math.exp(-delta / T):
            state = neighbor

        T *= k
        if T < 1e-6:
            break
    return state

solution = simulated_annealing(4)
print("Solution Reached:")
print_board(solution)
print(f"Conflicts: {cost(solution)}")
