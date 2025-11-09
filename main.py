board = [
    ['','',''],
    ['','',''],
    ['','','']
]
current_player = 'X'
def print_board(board):
    print("  1 2 3")
    for i, row in enumerate(board,start=1):
        print(i, end=' ')
        print('|'.join(row))
        if i < len(board):
            print("  -+-+-")

def get_move(player_symbol, board):
        while True:
            input_string = input(f"Игрок [{player_symbol}], ваш ход (строка, столбец):")
            if ',' in input_string and len(input_string) == 3:
                a1, b1 = input_string.split(',')
                a = int(a1)-1
                b = int(b1)-1
                if 0 <= a < 3 and 0 <= b < 3:
                    if board[a][b] == '':
                        return a, b
                    else:
                        print("Эта клетка уже занята, введите другую")
                else:
                    print("Ошибка. Введите числа в диапазоне от 1 до 3.")
            else:
                print("Ошибка. Числа написаны не через запятую или введено не 2 числа.")



def check_win(board, player_symbol):
    if board[0][0] == player_symbol and board[0][1] == player_symbol and board[0][2] == player_symbol:
        return True
    if board[1][0] == player_symbol and board[1][1] == player_symbol and board[1][2] == player_symbol:
        return True
    if board[2][0] == player_symbol and board[2][1] == player_symbol and board[2][2] == player_symbol:
        return True
    if board[0][0] == player_symbol and board[1][0] == player_symbol and board[2][0] == player_symbol:
        return True
    if board[0][1] == player_symbol and board[1][1] == player_symbol and board[2][1] == player_symbol:
        return True
    if board[0][2] == player_symbol and board[1][2] == player_symbol and board[2][2] == player_symbol:
        return True
    if board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == player_symbol:
        return True
    if board[0][2] == player_symbol and board[1][1] == player_symbol and board[2][0] == player_symbol:
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True


while True:
    print_board(board)
    row, col = get_move(current_player, board)
    board[row][col] = current_player
    if check_win(board, current_player):
            print(f"Игрок {current_player} победил!")
            print_board(board)
            break
    if check_draw(board):
            print("Ничья")
            print_board(board)
            break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

