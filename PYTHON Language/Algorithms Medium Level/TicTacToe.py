# Create a program that simulates a game of Tic Tac Toe. Users must be able to type a coordinate
# (Row,Column) to place the mark on the board.

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {' '.join(board[i])}")

def is_winner(board, player):
    # check rows
    for i in range(3):
        if board[i] == [player] * 3:
            return True
    # check columns
    for j in range(3):
        if [board[i][j] for i in range(3)] == [player] * 3:
            return True
    # check diagonals
    if [board[i][i] for i in range(3)] == [player] * 3:
        return True
    if [board[i][2-i] for i in range(3)] == [player] * 3:
        return True
    return False

def is_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    while True:
        print_board(board)
        player_input = input(f"{players[current_player]}'s turn. Enter row,col: ")
        try:
            row, col = map(int, player_input.split(','))
        except ValueError:
            print("Invalid input. Enter row,col with comma in between.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid input. Row and column must be between 0 and 2.")
            continue
        if board[row][col] != ' ':
            print("That cell is already taken.")
            continue
        board[row][col] = players[current_player]
        if is_winner(board, players[current_player]):
            print_board(board)
            print(f"{players[current_player]} wins!")
            return
        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            return
        current_player = (current_player + 1) % 2

play()
