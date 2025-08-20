import random

board = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

playcount = 0

def print_board():
    for row in board:
        print(' '.join(row))

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '-':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]

    return None

def minimax(is_computer):
    winner = check_winner()
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1

    # Check for draw
    if all(cell != '-' for row in board for cell in row):
        return 0

    if is_computer:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'O'
                    score = minimax(False)
                    board[row][col] = '-'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'X'
                    score = minimax(True)
                    board[row][col] = '-'
                    best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = 'O'
                score = minimax(False)
                board[row][col] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        board[row][col] = 'O'

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Try again.")
                continue
            row = move // 3
            col = move % 3
            if board[row][col] != '-':
                print("Cell already taken. Try again.")
                continue
            board[row][col] = 'X'
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

while True:
    print_board()
    player_move()
    playcount += 1
    winner = check_winner()
    if winner:
        print_board()
        print("You win!")
        break
    if playcount == 9:
        print_board()
        print("It's a draw!")
        break

    computer_move()
    playcount += 1
    winner = check_winner()
    if winner:
        print_board()
        print("Computer wins!")
        break
    if playcount == 9:
        print_board()
        print("It's a draw!")
        break
