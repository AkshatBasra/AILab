import random

# def clear_board():
#     global board
#     board = [['-', '-', '-'],
#              ['-', '-', '-'],
#              ['-', '-', '-']]

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

def winning_move():
    for row in range(3):
        if board[row].count('O') == 2 and board[row].count('-') == 1:
            print("Winning move found:", row, board[row])
            return (row, board[row].index('-'))
    for col in range(3):
        if ([board[0][col], board[1][col], board[2][col]].count('O') == 2 and 
            [board[0][col], board[1][col], board[2][col]].count('-') == 1):
            row = [board[0][col], board[1][col], board[2][col]].index('-')
            print("Winning move found:", row, col)
            return row, col
    left_diag = [board[0][0], board[1][1], board[2][2]]
    if left_diag.count('-') == 1 and left_diag.count('O') == 2:
        print("Winning move found in left diagonal:", left_diag)
        row = col = left_diag.index('-')
        return row, col
    right_diag = [board[0][2], board[1][1], board[2][0]]
    if right_diag.count('-') == 1 and right_diag.count('O') == 2:
        print("Winning move found in right diagonal:", right_diag)
        row = right_diag.index('-')
        col = 2 - right_diag.index('-')
        return row, col
    return None


def computer_move():
    move = winning_move()
    if move:
        row, col = move
        board[row][col] = 'O'
        return
    count = 0
    while count < 9:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '-':
            board[row][col] = 'O'
            break
        count += 1

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