# create board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

current_player = 'x'


# welcome
def welcome():
    print('welcome to dumbAss Tic Tac Toe')


# display board
def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def start():
    check_status()
    _ = ""
    print()
    print(current_player + "'s turn:")
    _ = input('enter the no (1 - 9) : ')
    try:
        _ = int(_)
        _ = _ - 1
        if _ in range(0, 9):
            if board[_] == '-':
                board[_] = current_player
                display_board()
                handle_player()
            else:
                print("u can't go there")
        else:
            print('wrong input')
        start()
    except Exception:
        print("invalid input")
        start()


def check_status():
    check_rows()
    check_columns()
    check_diagonals()
    check_tie()


def check_rows():
    if board[0] == board[1] == board[2] != '-':
        print(board[0] + " won")
        replay()
    if board[3] == board[4] == board[5] != '-':
        print(board[3] + " won")
        replay()
    if board[6] == board[7] == board[8] != '-':
        print(board[6] + " won")
        replay()


def check_columns():
    if board[0] == board[3] == board[6] != '-':
        print(board[0] + " won")
        replay()
    if board[1] == board[4] == board[7] != '-':
        print(board[1] + " won")
        replay()
    if board[2] == board[5] == board[8] != '-':
        print(board[2] + " won")
        replay()


def check_diagonals():
    if board[0] == board[4] == board[8] != '-':
        print(board[0] + " won")
        replay()
    if board[2] == board[4] == board[6] != '-':
        print(board[2] + " won")
        replay()


def check_tie():
    if '-' not in board:
        print('tie')
        replay()


def handle_player():
    global current_player
    if current_player == 'x':
        current_player = '0'
    elif current_player == '0':
        current_player = 'x'


def replay():
    print()
    print("1) to replay")
    print("0) to exit")
    rep = input("enter u r choice :")
    try:
        if rep == '1':
            print()
            print('-----------------')
            print()
            global board
            board = ['-', '-', '-',
                     '-', '-', '-',
                     '-', '-', '-']
            display_board()
            start()
        elif rep == '0':
            print('have a nice day')
            exit()
        else:
            print("invalid input")
            replay()
    except Exception:
        print("invalid input")
        replay()


def main():
    welcome()
    display_board()
    start()


main()
