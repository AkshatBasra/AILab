import math

def print_board(board):
    print()
    for i in range(1, 10, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

def check_winner(board):
    win_positions = [
        (1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7)
    ]
    for (x, y, z) in win_positions:
        if board[x] == board[y] == board[z] != ' ':
            return board[x]
    if all(board[i] != ' ' for i in range(1,10)):
        return 'Draw'
    return None

def alphabeta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'X'
                score = alphabeta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'O'
                score = alphabeta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = 'X'
            score = alphabeta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' '] * 10
    print("Tic Tac Toe — You (O) vs Computer (X)")
    print("Positions:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")

    turn = input("\nDo you want to play first? (y/n): ").lower()
    human_first = (turn == 'n')

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        if (board.count(' ') % 2 == (0 if human_first else 1)):
            move = best_move(board)
            board[move] = 'X'
            print(f"Computer chooses position {move}")
        else:
            try:
                move = int(input("Enter your move (1-9): "))
                if 1 <= move <= 9 and board[move] == ' ':
                    board[move] = 'O'
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

if __name__ == "__main__":
    play_game()
