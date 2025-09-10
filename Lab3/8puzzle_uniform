import heapq
import time

# Goal state
GOAL = [[1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]]  # 0 = blank

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

# Uniform Cost Search
def uniform_cost_search(start):
    open = []
    heapq.heappush(open, (0, start, []))  # (priority=g, g, state, path)
    closed = set()

    while open:
        g, state, path = heapq.heappop(open)
        if state == GOAL:
            return path + [state]

        state_id = state_to_tuple(state)
        if state_id in closed:
            continue
        closed.add(state_id)

        for next in neighbors(state):
            heapq.heappush(open, (g+1, next, path + [state]))

    return None


# Print board
def print_board(board):
    for row in board:
        print(row)
    print()

# Example usage
start_state = [[3, 2, 8],
               [4, 0, 7],
               [1, 5, 6]]
print("Random Start State:")
print_board(start_state)

start = time.time()
solution = uniform_cost_search(start_state)
end = time.time()

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        print_board(step)
    print("Time taken: ", end - start)
else:
    print("No solution exists")
