import heapq
import random

# Goal state
GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]  # 0 = blank

# Directions (row, col)
moves = [(-1,0), (1,0), (0,-1), (0,1)]

# Heuristic: Manhattan Distance
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val-1, 3)
                dist += abs(goal_x - i) + abs(goal_y - j)
    return dist

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next states
def neighbors(state):
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state

# Convert list to tuple (for visited set)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Search
def astar(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))  # (f, g, state, path)
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == GOAL:
            return path + [state]

        state_id = state_to_tuple(state)
        if state_id in visited:
            continue
        visited.add(state_id)

        for nxt in neighbors(state):
            heapq.heappush(pq, (g+1 + manhattan(nxt), g+1, nxt, path + [state]))

    return None

# Create a random solvable board
def create_random_board():
    nums = list(range(9))
    while True:
        random.shuffle(nums)
        board = [nums[i*3:(i+1)*3] for i in range(3)]
        if is_solvable(board):
            return board

# Count inversions to check solvability
def is_solvable(board):
    flat = sum(board, [])
    inv = 0
    for i in range(9):
        for j in range(i+1, 9):
            if flat[i] and flat[j] and flat[i] > flat[j]:
                inv += 1
    return inv % 2 == 0

# Print board
def print_board(board):
    for row in board:
        print(row)
    print()

# Example usage
start_state = create_random_board()
print("Random Start State:")
print_board(start_state)

solution = astar(start_state)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        print_board(step)
else:
    print("No solution exists")
